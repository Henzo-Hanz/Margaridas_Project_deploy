# 🚀 Guia de Teste - Margarida's Treasury v2.0

## Pré-requisitos
- Ambiente virtual ativado
- Servidor rodando: `python backend/run.py`

## Passos para Testar

### 1️⃣ Inicializar o Banco de Dados
```bash
python backend/scripts/init_db.py
```
**Esperado**: Mensagem indicando que o usuário "Margarida" foi criado ou já existe

### 2️⃣ Iniciar o Servidor
```bash
python backend/run.py
```
**Esperado**: Servidor rodando em `http://localhost:8000`

### 3️⃣ Acessar a Aplicação
1. Abra no navegador: `http://localhost:8000/`
2. Clique em "Entrar com Senhas" ou acesse `/login`

### 4️⃣ Login
- **Email**: `margarida@example.com`
- **Senha**: `senha_secreta_123`
- **Esperado**: Redirecionamento para `/dashboard`

### 5️⃣ Testar Dashboard
✅ Dois cards aparecem:
- 🌷 Margarida's Garden
- 💎 Margarida's Treasury

✅ Clique em cada um para navegar

### 6️⃣ Testar Treasury - Despesas
1. Na aba "📊 Despesas":
   - Descrição: "Supermercado"
   - Valor: "150.50"
   - Data: Selecione uma data
   - Método: "Cartão"
   - Clique: "Registrar Despesa"

**Esperado**: 
- A despesa aparece na lista abaixo
- Pode editar ou deletar

### 7️⃣ Testar Treasury - Receitas
1. Na aba "💰 Receitas":
   - Descrição: "Salário"
   - Valor: "3000.00"
   - Data: Selecione uma data
   - Clique: "Registrar Receita"

**Esperado**: 
- A receita aparece na lista
- Pode editar ou deletar

### 8️⃣ Testar Análises
1. Clique na aba "📈 Análises"

**Esperado**:
- ✅ Resumo de 3, 6, 12 meses
- ✅ Gráfico Doughnut de métodos de pagamento
- ✅ Gráfico Bar comparando Despesas vs Receitas

### 9️⃣ Testar Navegação
- ✅ Botão "Voltar" retorna ao dashboard
- ✅ Botão "Sair" desconecta e volta ao login
- ✅ Logo leva de volta ao início

## 🔍 Testes de Validação

### Campos Obrigatórios
- [ ] Tente registrar sem preencher "Descrição" → Erro
- [ ] Tente com valor 0 ou negativo → Erro
- [ ] Sem data → Usa data atual automaticamente ✅

### Edição/Deleção
- [ ] Clique em ✏️ para editar
- [ ] Form preenche com dados anteriores
- [ ] Clique em 🗑️ para deletar → Confirma antes de deletar

### Gráficos
- [ ] Registre despesas com métodos diferentes
- [ ] Veja gráfico de métodos se atualizar
- [ ] Gráfico mensal combina dados corretamente

## 📱 Testes Responsivos
- [ ] Desktop (1200px+)
- [ ] Tablet (768px - 1199px)
- [ ] Mobile (< 768px) - Cards empilhados

## 🐛 Debug
Se encontrar erros:

1. **Console do navegador** (F12 → Console)
   - Veja erros de JavaScript
   - Veja requisições de rede

2. **Terminal do servidor**
   - Logs de aplicação
   - Erros de API

3. **Banco de dados**
   ```bash
   # Verifique tabelas
   python backend/scripts/init_db.py
   ```

## ✅ Checklist de Sucesso
- [ ] Dashboard aparece após login
- [ ] Despesa pode ser registrada
- [ ] Receita pode ser registrada
- [ ] Gráficos aparecem com dados
- [ ] Cálculos de totais estão corretos
- [ ] Edição e deleção funcionam
- [ ] Navegação entre abas funciona
- [ ] Responsivo em mobile
- [ ] Logout funciona corretamente

## 💡 Dicas

1. **Registre vários datos** com datas diferentes para ver gráficos melhores
2. **Use diferentes métodos** de pagamento para ver gráfico mais interessante
3. **Limpe o localStorage** se quiser resetar: `localStorage.clear()` no console
4. **Teste períodos** (3m, 6m, 12m) registrando dados em meses diferentes

---

**Dúvidas?** Verifique `ATUALIZACOES_v2.md` para documentação completa
