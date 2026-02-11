# ⚡ Quick Start - Margarida's Garden v2.0

## 🚀 Comece Aqui (5 minutos)

### Passo 1: Abra PowerShell/Terminal
```bash
cd "c:\Users\USER2NOTE069\Desktop\Python\Margarida's_Garden_Project"
```

### Passo 2: Ative Ambiente Virtual
```bash
.venv\Scripts\Activate.ps1
```

### Passo 3: Inicialize Banco de Dados
```bash
python backend/scripts/init_db.py
```

**Esperado:**
```
Usuário 'Margarida' criado com sucesso!
  Email: margarida@example.com
  Senha: senha_secreta_123
```

### Passo 4: Inicie Servidor
```bash
python backend/run.py
```

**Esperado:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Passo 5: Abra Navegador
```
http://localhost:8000/
```

✅ **Pronto! Você está online!**

---

## 📱 Testando a Aplicação

### 1️⃣ Faça Login
- Email: `margarida@example.com`
- Senha: `senha_secreta_123`

### 2️⃣ Você verá um Dashboard
- 🌷 Margarida's Garden (Senhas)
- 💎 Margarida's Treasury (Finanças) **NOVO!**

### 3️⃣ Clique em "Margarida's Treasury"

### 4️⃣ Teste as Funcionalidades
- **Despesas**: Registre uma despesa
- **Receitas**: Registre uma receita
- **Análises**: Veja gráficos

---

## 🆘 Problemas?

### Erro: "Porta 8000 em uso"
```bash
# Mude para outra porta em backend/run.py
python -m uvicorn app.main:app --port 9000
# ou
ngrok http 8000  # usar em outra máquina
```

### Erro: "ModuleNotFoundError"
```bash
# Certifique-se que venv está ativado
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Erro: "Banco de dados corrompido"
```bash
del margarida_garden.db
python backend/scripts/init_db.py
```

---

## 📚 Próximos Documentos

| Documento | Quando Ler |
|-----------|-----------|
| [`ATUALIZACOES_v2.md`](ATUALIZACOES_v2.md) | Depois de login bem-sucedido |
| [`GUIA_TESTE_v2.md`](GUIA_TESTE_v2.md) | Antes de usar as features |
| [`CONFIGURACAO.md`](CONFIGURACAO.md) | Se encontrar problemas |
| [`MAPA_NAVEGACAO.md`](MAPA_NAVEGACAO.md) | Para visualizar fluxos |

---

## ✨ O Que É Novo (v2.0)

✅ Dashboard intermediário após login  
✅ Novo app: Margarida's Treasury  
✅ Registre despesas e receitas  
✅ Veja gráficos de análise  
✅ Calcule seus gastos mensais  

---

## 🎯 Resumo 1-Minuto

1. `python backend/scripts/init_db.py` - Cria banco
2. `python backend/run.py` - Inicia servidor
3. `localhost:8000` - Abra no navegador
4. Login com padrão
5. Explore! 🚀

---

## 💡 Dicas

### Criar múltiplos gastos
- Clique "Despesas"
- Registre vários com datas diferentes
- Veja no gráfico como aparecem

### Testar gráficos
- Registre despesas com diferentes métodos
- Na aba Análises veja o gráfico atualizar

### Resetar banco
```bash
del margarida_garden.db
python backend/scripts/init_db.py
```

---

## ✅ Checklist Rápido

- [ ] Venv ativado
- [ ] Banco criado
- [ ] Servidor rodando
- [ ] Login funciona  
- [ ] Dashboard aparece
- [ ] Treasury abre
- [ ] Pode registrar despesa
- [ ] Gráficos mostram dados

---

**Status**: ✅ Tudo pronto!

**Próximo**: Siga `GUIA_TESTE_v2.md` para teste completo
