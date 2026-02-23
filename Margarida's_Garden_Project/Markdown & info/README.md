# 🌷 Margarida's Garden & Treasury - v2.0

Uma suite completa de aplicativos pessoais com gerenciamento de senhas e finanças.

## 📱 Aplicativos

### 🌷 Margarida's Garden
Gerenciador de senhas amigável, seguro e confiável com UI intuitiva.
- Armazene senhas criptografadas
- Organize por serviço
- Interface responsiva

### 💎 Margarida's Treasury (NOVO v2.0)
Gestor de finanças pessoais completo.
- Registre despesas e receitas
- Análise financial detalhada
- Gráficos interativos
- 3 períodos de análise (3m, 6m, 12m)

## ⚡ Início Rápido

```bash
# 1. Criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Inicializar banco de dados
python backend/scripts/init_db.py

# 4. Executar servidor
python backend/run.py
```

Acesse: **http://localhost:8000**

## 🔑 Credenciais Padrão

| Campo | Valor |
|-------|-------|
| **Email** | margarida@example.com |
| **Senha** | senha_secreta_123 |
| **Nome** | Margarida |

## ✨ Funcionalidades v2.0

### Dashboard (NOVO)
- Página intermediária após login
- Seleção entre aplicativos
- Cards temáticos e intuitivos

### Margarida's Garden
- ✅ Landing page com animação de flores
- ✅ Login com JWT
- ✅ CRUD de senhas
- ✅ Senhas criptografadas
- ✅ Interface responsiva

### Margarida's Treasury (NOVO)
- ✅ Registrar despesas (6 métodos de pagamento)
- ✅ Registrar receitas
- ✅ Editar e deletar
- ✅ Análise financeira por períodos
- ✅ 2 Gráficos interativos
- ✅ Resumo de balanço

## 📊 Endpoints da API

### Despesas (5)
- `POST /api/treasury/expenses`
- `GET /api/treasury/expenses`
- `GET /api/treasury/expenses/{id}`
- `PUT /api/treasury/expenses/{id}`
- `DELETE /api/treasury/expenses/{id}`

### Receitas (5)
- `POST /api/treasury/incomes`
- `GET /api/treasury/incomes`
- `GET /api/treasury/incomes/{id}`
- `PUT /api/treasury/incomes/{id}`
- `DELETE /api/treasury/incomes/{id}`

### Análises (3)
- `GET /api/treasury/analytics/summary`
- `GET /api/treasury/analytics/by-method`
- `GET /api/treasury/analytics/monthly`

**Total: 19 Novos Endpoints**

## 📁 Estrutura

```
Margarida's_Garden_Project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── credentials.py
│   │   │   └── treasury.py (NOVO)
│   │   ├── core/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── credential.py
│   │   │   ├── expense.py (NOVO)
│   │   │   └── income.py (NOVO)
│   │   ├── schemas/
│   │   │   ├── expense.py (NOVO)
│   │   │   └── income.py (NOVO)
│   │   └── main.py (Atualizado)
│   ├── scripts/
│   └── alembic/
├── frontend/
│   ├── static/
│   │   ├── css/ (Atualizado)
│   │   └── js/
│   └── templates/
│       ├── login.html (Atualizado)
│       ├── dashboard.html (NOVO)
│       ├── treasury.html (NOVO)
│       └── garden.html
├── requirements.txt
├── README.md
├── CHANGELOG.md (Novo)
├── CONFIGURACAO.md (Novo)
└── ATUALIZACOES_v2.md (Novo)
```

## 🚀 Tech Stack

### Backend
- **FastAPI** - Framework web
- **SQLAlchemy** - ORM
- **Pydantic** - Validação
- **JWT** - Autenticação
- **Bcrypt** - Hash de senhas

### Frontend
- **Jinja2** - Templates
- **HTML5** - Markup
- **CSS3** - Styling
- **Vanilla JS** - Interatividade
- **Chart.js** - Gráficos

### Banco de Dados
- **SQLite** - Desenvolvimento
- **PostgreSQL** - Produção (compatível)

## 🎨 Design

- Tema pastel temático
- Cores consistentes
- UI intuitiva
- Completamente responsivo
- Animações suaves

## 📚 Documentação

- [`CONFIGURACAO.md`](CONFIGURACAO.md) - Setup detalhado
- [`GUIA_TESTE_v2.md`](GUIA_TESTE_v2.md) - Guia de testes
- [`ATUALIZACOES_v2.md`](ATUALIZACOES_v2.md) - O que é novo
- [`CHANGELOG.md`](CHANGELOG.md) - Histórico completo
- [`RESUMO_IMPLEMENTACAO.md`](RESUMO_IMPLEMENTACAO.md) - Sumário visual

## 🔒 Segurança

- ✅ Autenticação JWT
- ✅ Senhas com Bcrypt
- ✅ SQL Injection protection
- ✅ CORS configurado
- ✅ Validação de entrada
- ✅ XSS protection

## 📱 Compatibilidade

- ✅ Chrome/Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)
- ✅ Mobile browsers
- ✅ Tablets
- ✅ Desktops

## 🧪 Como Testar

```bash
# Seguir GUIA_TESTE_v2.md
```

## 📞 Troubleshooting

Veja `CONFIGURACAO.md` para:
- Resolver problemas comuns
- Resetar banco de dados
- Mudar porta do servidor
- Configurar variáveis de ambiente

## 🔄 Atualização do v1.0

Atualize automaticamente:
```bash
git pull
pip install -r requirements.txt
python backend/scripts/init_db.py
```

Compatível 100% com dados existentes! ✅

## 📊 Estatísticas

- **Versão**: 2.0.0
- **Status**: ✅ Pronto para Produção
- **Código Backend**: ~800 linhas (novo)
- **Código Frontend**: ~1200 linhas (novo)
- **Documentação**: ~1000 linhas (novo)
- **Novos Endpoints**: 19
- **Gráficos**: 2

## 🎯 Próximas Melhorias

- [ ] Exportar em CSV/PDF
- [ ] Categorias customizáveis
- [ ] Metas financeiras
- [ ] Relatórios automáticos por email
- [ ] Modo escuro
- [ ] Multi-moeda

## 📄 Licença

MIT License - Use livremente

## 🙋 Suporte

Para dúvidas, consulte os documentos:
- CONFIGURACAO.md
- GUIA_TESTE_v2.md
- ATUALIZACOES_v2.md

---
 
**Versão 2.0.0 - Fevereiro 2026**
