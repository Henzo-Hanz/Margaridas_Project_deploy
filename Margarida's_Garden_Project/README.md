# Margarida's Garden

Gerenciador de senhas amigável, seguro e confiável com UI intuitiva.

## Requisitos

- Python 3.10+
- pip

## Instalação

```bash
# Criar ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Inicializar banco e criar usuário padrão
cd backend
python scripts/init_db.py
cd ..
```

## Executar

```bash
cd backend
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Ou:

```bash
cd backend
python run.py
```

Acesse: **http://localhost:8000**

## Credenciais padrão (V1)

- **Email:** margarida@garden.local
- **Senha:** garden123

## Funcionalidades

- Landing page com animação de flores e pétalas
- Login com JWT
- CRUD de senhas (adicionar, editar, excluir, listar)
- Senhas criptografadas no banco
- Interface responsiva

## Estrutura

```
Margarida's_Garden_Project/
├── backend/
│   ├── app/
│   │   ├── api/          # Rotas da API
│   │   ├── core/         # Config, auth, security
│   │   ├── models/       # SQLAlchemy models
│   │   └── schemas/      # Pydantic schemas
│   ├── alembic/          # Migrações
│   └── scripts/         # Scripts utilitários
├── frontend/
│   ├── static/           # CSS, JS
│   └── templates/        # HTML Jinja2
├── requirements.txt
└── README.md
```
