# ⚙️ Guia de Configuração - Margarida's Garden v2.0

## 🚀 Começar Rápido

### Passo 1: Ativar Ambiente Virtual
```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# ou Windows CMD
.venv\Scripts\activate.bat

# ou Linux/Mac
source .venv/bin/activate
```

### Passo 2: Instalar Dependências (se necessário)
```bash
pip install -r requirements.txt
```

### Passo 3: Inicializar Banco de Dados
```bash
python backend/scripts/init_db.py
```

**Saída esperada:**
```
Usuário 'Margarida' criado com sucesso!
  Email: margarida@example.com
  Senha: senha_secreta_123
```

### Passo 4: Iniciar Servidor
```bash
python backend/run.py
```

**Saída esperada:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Passo 5: Acessar no Navegador
```
http://localhost:8000/
```

## 📋 Credenciais Padrão

| Campo | Valor |
|-------|-------|
| **Email** | margarida@example.com |
| **Senha** | senha_secreta_123 |
| **Nome** | Margarida |

## 🔧 Variáveis de Ambiente

Se precisar, edite `backend/app/core/config.py`:

```python
# Usuario padrão
DEFAULT_USER_NAME = "Margarida"
DEFAULT_USER_EMAIL = "margarida@example.com"
DEFAULT_USER_PASSWORD = "senha_secreta_123"

# JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# Banco de dados
DATABASE_URL = "sqlite:///./margarida_garden.db"
```

## 📁 Estrutura de Diretórios Criados

Após inicializar o banco, será criado:
```
margarida_garden.db          (Banco SQLite)
alembic/versions/            (Migrations)
__pycache__/                 (Cache Python)
.venv/                       (Ambiente Virtual)
```

## 🧹 Limpeza e Reset

### Deletar Banco e Resetar
```bash
# Windows
del margarida_garden.db
python backend/scripts/init_db.py

# Linux/Mac
rm margarida_garden.db
python backend/scripts/init_db.py
```

### Limpar Cache Python
```bash
# Windows
for /D %x in (.\*\__pycache__) do @rd /s /q "%x"

# Linux/Mac
find . -name __pycache__ -type d -exec rm -r {} +
```

## 🐛 Troubleshooting

### Problema: "ModuleNotFoundError"
**Solução:**
```bash
# Certifique-se que o venv está ativado
.venv\Scripts\Activate.ps1

# Instale dependências
pip install -r requirements.txt
```

### Problema: Porta 8000 já em uso
**Solução:**
```python
# Edite backend/run.py
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000)  # Mude para 9000
```

### Problema: Banco de dados corrompido
**Solução:**
```bash
# Delete e recrie
del margarida_garden.db
python backend/scripts/init_db.py
```

### Problema: Erro de CORS
**Solução:** O CORS já está configurado permissivamente em `main.py`. Se precisar restringir:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://seu-dominio.com"],  # Especifique seus domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📊 Verificar Banco de Dados

### Com SQLite CLI
```bash
# Instale sqlite3
pip install sqlite-utils

# Verifique tabelas
sqlite3 margarida_garden.db ".tables"

# Verifique usuários
sqlite3 margarida_garden.db "SELECT * FROM users;"
```

### Com Python
```python
from app.core.database import SessionLocal
from app.models.user import User

db = SessionLocal()
users = db.query(User).all()
for user in users:
    print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}")
db.close()
```

## 🌐 Rotas Principais

| Rota | Descrição | Requer Auth |
|------|-----------|-------------|
| `/` | Landing page | ❌ |
| `/login` | Página de login | ❌ |
| `/dashboard` | Seletor de apps | ✅ |
| `/garden` | Gerenciador de senhas | ✅ |
| `/treasury` | Gerenciador de finanças | ✅ |
| `/api/*` | Endpoints de API | ✅ |

## 🎯 URLs Úteis

```
Web Interface:
- http://localhost:8000/                 Landing
- http://localhost:8000/login            Login
- http://localhost:8000/dashboard        Seletor
- http://localhost:8000/garden           Jardim
- http://localhost:8000/treasury         Tesouro

API Documentation:
- http://localhost:8000/docs             Swagger UI (automático)
- http://localhost:8000/redoc            ReDoc (automático)

API Base:
- http://localhost:8000/api/             Base de APIs
```

## 📦 Docker (Opcional)

Se quiser containerizar:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ ./backend
COPY frontend/ ./frontend

CMD ["python", "backend/run.py"]
```

## 🔒 Segurança em Produção

Antes de fazer deploy:

1. **Mude a senha padrão**
   ```python
   # backend/app/core/config.py
   DEFAULT_USER_PASSWORD = "sua_senha_super_segura_123"
   ```

2. **Use HTTPS**
   ```python
   # Adicione configuração SSL
   ```

3. **Use banco de dados real**
   ```python
   DATABASE_URL = "postgresql://user:pass@localhost/margarida"
   ```

4. **Implemente rate limiting**
   ```python
   from slowapi import Limiter
   from slowapi.util import get_remote_address
   ```

5. **Adicione logging**
   ```python
   import logging
   logging.basicConfig(filename='app.log', level=logging.INFO)
   ```

## 📱 Testar em Dispositivos

### Mesmo WiFi
```bash
# Descubra seu IP
ipconfig getifaddr en0  # Mac
ipconfig             # Windows
hostname -I          # Linux

# Acesse de outro dispositivo
http://seu_ip:8000/
```

### Testing Tools
```bash
# Teste endpoints API
curl http://localhost:8000/api/auth/login -X POST

# Com autenticação
curl -H "Authorization: Bearer TOKEN" \
     http://localhost:8000/api/treasury/expenses
```

## 📈 Monitoramento

### Logs do Servidor
Estão no console onde o servidor está rodando. Para salvar:

```python
# backend/run.py
import logging

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Métricas de Performance
- Tempo de resposta API
- Uso de memória
- Quantidade de requisições

## 🧬 Git & Versionamento

```bash
# Status
git status

# Commit
git add .
git commit -m "feat: Adicionar Margarida's Treasury v2.0"

# Push
git push origin main
```

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os logs** - Procure por erros no console
2. **Teste com Swagger** - http://localhost:8000/docs
3. **Inspecione o navegador** - F12 → Console e Network
4. **Verifique o banco** - Veja se as tabelas foram criadas

---

**✅ Parabéns! Sua aplicação está pronta para usar!**

Próximo: Leia `GUIA_TESTE_v2.md` para começar a testar
