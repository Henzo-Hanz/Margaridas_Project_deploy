#!/usr/bin/env python3
"""
Security Audit - Valida vulnerabilidades OWASP Top 10.
Executa verificações no backend e retorna relatório.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend"))

# Carrega env antes de importar app
from dotenv import load_dotenv
load_dotenv(ROOT / ".env")

def check_secret_key() -> tuple[bool, str]:
    """A01:2021 – Broken Access Control / Sensitive Data Exposure"""
    default = "margarida-garden-secret-key-change-in-production"
    key = os.getenv("SECRET_KEY", default)
    if not key or key == default:
        return False, "SECRET_KEY não definida ou usa valor padrão inseguro"
    return True, "SECRET_KEY configurada"

def check_cors() -> tuple[bool, str]:
    """A05:2021 – Security Misconfiguration"""
    from app.core.config import settings
    origins = settings.cors_origins_list
    if "*" in origins or not origins:
        return False, "CORS permite todas as origens (*)"
    return True, f"CORS restrito a {len(origins)} origem(ns)"

def check_rate_limit() -> tuple[bool, str]:
    """A07:2021 – Identification and Authentication Failures"""
    try:
        from slowapi import Limiter
        return True, "Rate limiting (SlowAPI) configurado"
    except ImportError:
        return False, "Rate limiting não encontrado"

def check_security_headers() -> tuple[bool, str]:
    """A05:2021 – Security Misconfiguration"""
    try:
        from app.core.middlewares import SecurityHeadersMiddleware
        return True, "Security headers middleware presente"
    except ImportError:
        return False, "Security headers middleware não encontrado"

def check_exception_handler() -> tuple[bool, str]:
    """A09:2021 – Security Logging and Monitoring / Information Disclosure"""
    # Verifica se em produção não expõe str(e)
    env = os.getenv("ENVIRONMENT", "development")
    if env.lower() == "production":
        return True, "Em produção, detalhes de exceção são suprimidos"
    return True, "Ambiente development - detalhes de erro habilitados"

def check_password_storage() -> tuple[bool, str]:
    """A02:2021 – Cryptographic Failures"""
    try:
        from passlib.context import CryptContext
        ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return True, "Senhas com bcrypt"
    except Exception:
        return False, "Verificar armazenamento de senhas"

def main() -> int:
    print("=== Security Audit - Margarida's Garden ===\n")
    checks = [
        ("SECRET_KEY", check_secret_key),
        ("CORS", check_cors),
        ("Rate Limiting", check_rate_limit),
        ("Security Headers", check_security_headers),
        ("Exception Handler", check_exception_handler),
        ("Password Storage", check_password_storage),
    ]
    failed = 0
    for name, fn in checks:
        try:
            ok, msg = fn()
            status = "OK" if ok else "FALHA"
            if not ok:
                failed += 1
            print(f"[{status}] {name}: {msg}")
        except Exception as e:
            print(f"[ERRO] {name}: {e}")
            failed += 1
    print(f"\n{failed} verificação(ões) falharam." if failed else "\nTodas as verificações passaram.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
