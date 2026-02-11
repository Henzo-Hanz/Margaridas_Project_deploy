# Como Rodar o Projeto Margarida's Garden

## Opção mais fácil: Tudo de uma vez

Execute **instalar_e_rodar.bat** — ele cria o .venv (se não existir), instala as dependências, inicializa o banco e inicia o servidor.

## Opção 1: Comandos manuais

### 1. Inicializar banco de dados:
```bash
cd backend
python scripts\init_db.py
```

### 2. Iniciar servidor:
```bash
cd backend
python run.py
```

Ou usando uvicorn diretamente:
```bash
cd backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Acessar a aplicação

Após iniciar o servidor, acesse:

- **Landing Page:** http://localhost:8000
- **Login:** http://localhost:8000/login
- **Jardim (após login):** http://localhost:8000/garden
- **API Docs:** http://localhost:8000/docs

## Credenciais padrão

- **Email:** margarida@garden.local
- **Senha:** garden123

## Verificar se está rodando

O servidor estará rodando quando você ver mensagens como:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

## Parar o servidor

Pressione `Ctrl+C` no terminal onde o servidor está rodando.
