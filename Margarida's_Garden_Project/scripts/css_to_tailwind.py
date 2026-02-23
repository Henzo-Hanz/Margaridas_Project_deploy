#!/usr/bin/env python3
"""
Migra style.css para Tailwind CSS personalizado.
Gera: tailwind.config.js (theme.extend), components.css (@layer), migration-map.json.

Uso:
  python scripts/css_to_tailwind.py frontend/static/css/style.css --html-dir frontend/templates/ --output-dir frontend/
"""
import argparse
import json
import re
from pathlib import Path


def parse_root_vars(css: str) -> dict[str, str]:
    """Extrai variáveis :root { --name: value; }"""
    vars_ = {}
    root_match = re.search(r":root\s*\{([^}]+)\}", css, re.DOTALL)
    if root_match:
        for match in re.finditer(r"--([a-zA-Z0-9-]+)\s*:\s*([^;]+);", root_match.group(1)):
            vars_[match.group(1)] = match.group(2).strip()
    return vars_


def extract_classes_from_html(html_dir: Path) -> set[str]:
    """Extrai classes de arquivos HTML/Jinja."""
    classes: set[str] = set()
    if not html_dir or not html_dir.exists():
        return classes
    for f in html_dir.rglob("*.html"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'class=["\']([^"\']+)["\']', content):
            for c in re.split(r"\s+", m.group(1)):
                c = c.strip()
                if c and "{{" not in c:
                    classes.add(c)
        for m in re.finditer(r"class=\{\{.*?\}\}\s+([^"\'>\s]+)", content):
            classes.add(m.group(1).strip())
    return classes


def parse_css_rules(css: str) -> dict[str, str]:
    """Extrai regras .class { ... } (seletor simples)."""
    rules: dict[str, str] = {}
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    for m in re.finditer(r"\.([a-zA-Z_][a-zA-Z0-9_-]*)\s*\{([^}]+)\}", css):
        selector = m.group(1)
        if selector not in ("root",):
            body = m.group(2).strip()
            rules[selector] = body
    return rules


def css_prop_to_tailwind(prop: str, val: str, vars_: dict) -> str | None:
    """Mapeia propriedade CSS para classe Tailwind (simplificado)."""
    prop = prop.strip().lower()
    val = val.strip()
    if prop == "display":
        if val == "flex":
            return "flex"
        if val == "grid":
            return "grid"
        if val == "none":
            return "hidden"
    if prop == "flex-direction" and val == "column":
        return "flex-col"
    if prop in ("align-items", "justify-content"):
        m = {"center": "center", "flex-start": "start", "flex-end": "end", "space-between": "between"}
        v = m.get(val.split()[0] if val else "", val)
        if prop == "align-items":
            return f"items-{v}" if v in m else None
        return f"justify-{v}" if v in m else None
    if prop == "padding" and re.match(r"^\d+rem$", val):
        n = int(re.search(r"\d+", val).group())
        return f"p-{n * 4}"
    if prop == "margin" and re.match(r"^\d+rem\s+0", val):
        return None
    if prop == "text-align" and val == "center":
        return "text-center"
    if prop == "font-weight":
        if val == "600":
            return "font-semibold"
        if val == "400":
            return "font-normal"
    if prop == "width" and val == "100%":
        return "w-full"
    if prop == "min-height" and val == "100vh":
        return "min-h-screen"
    if prop == "position" and val == "relative":
        return "relative"
    if prop == "position" and val == "absolute":
        return "absolute"
    return None


def vars_to_tailwind_theme(vars_: dict) -> dict:
    """Converte variáveis CSS em theme.extend para tailwind.config."""
    colors = {}
    for k, v in vars_.items():
        if "flower" in k or "grass" in k or "sky" in k or "text" in k:
            name = k.replace("--", "").replace("-", "_")
            colors[name] = v
    return {"colors": colors} if colors else {}


def build_migration_map(
    used_classes: set[str],
    rules: dict[str, str],
    vars_: dict,
) -> dict[str, str]:
    """Gera mapeamento classe-antiga -> classes-tailwind ou componente."""
    mapping: dict[str, str] = {}
    for cls in sorted(used_classes):
        if cls not in rules:
            continue
        body = rules[cls]
        parts = []
        for decl in re.finditer(r"([a-zA-Z-]+)\s*:\s*([^;]+);", body):
            tw = css_prop_to_tailwind(decl.group(1), decl.group(2), vars_)
            if tw:
                parts.append(tw)
        if parts:
            mapping[cls] = " ".join(parts)
        else:
            mapping[cls] = f"@apply-component {cls}"
    return mapping


def generate_components_css(
    used_classes: set[str],
    rules: dict[str, str],
    vars_: dict,
) -> str:
    """Gera CSS com @layer components para classes complexas."""
    lines = ["@layer components {", ""]
    for cls in sorted(used_classes):
        if cls not in rules:
            continue
        body = rules[cls]
        tw_approx = []
        for decl in re.finditer(r"([a-zA-Z-]+)\s*:\s*([^;]+);", body):
            tw = css_prop_to_tailwind(decl.group(1), decl.group(2), vars_)
            if tw:
                tw_approx.append(tw)
        if len(tw_approx) >= 3:
            lines.append(f"  .{cls} {{")
            lines.append(f"    @apply {' '.join(tw_approx)};")
            lines.append("  }")
            lines.append("")
        elif "animation" in body or "@" in body or "gradient" in body.lower():
            lines.append(f"  .{cls} {{")
            for decl in re.finditer(r"([a-zA-Z-]+)\s*:\s*([^;]+);", body):
                lines.append(f"    {decl.group(1)}: {decl.group(2).strip()};")
            lines.append("  }")
            lines.append("")
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Migra CSS para Tailwind")
    parser.add_argument("css_file", type=Path, help="Arquivo CSS de entrada")
    parser.add_argument("--html-dir", type=Path, default=None, help="Pasta de templates HTML")
    parser.add_argument("--output-dir", type=Path, default=Path("frontend"), help="Pasta de saída")
    args = parser.parse_args()

    css_path = args.css_file
    if not css_path.exists():
        print(f"Erro: {css_path} não encontrado")
        return

    css = css_path.read_text(encoding="utf-8", errors="ignore")
    vars_ = parse_root_vars(css)
    rules = parse_css_rules(css)
    used_classes = extract_classes_from_html(args.html_dir) if args.html_dir else set(rules.keys())

    out_dir = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    theme = vars_to_tailwind_theme(vars_)
    config = {
        "content": ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
        "theme": {"extend": theme} if theme else {},
        "plugins": [],
    }

    config_path = out_dir / "tailwind.config.js"
    config_path.write_text(
        f"""/** Gerado por css_to_tailwind.py - Margarida's Garden */
export default {{
  content: ['./index.html', './src/**/*.{{js,ts,jsx,tsx}}'],
  theme: {{
    extend: {json.dumps(theme, indent=6) if theme else "{}"}
  }},
  plugins: []
}}
""",
        encoding="utf-8",
    )
    print(f"Gerado: {config_path}")

    migration = build_migration_map(used_classes, rules, vars_)
    map_path = out_dir / "migration-map.json"
    map_path.write_text(json.dumps(migration, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Gerado: {map_path}")

    src_styles = out_dir / "src" / "styles"
    src_styles.mkdir(parents=True, exist_ok=True)
    components = generate_components_css(used_classes, rules, vars_)
    components_path = src_styles / "components.css"
    components_path.write_text(components, encoding="utf-8")
    print(f"Gerado: {components_path}")


if __name__ == "__main__":
    main()
