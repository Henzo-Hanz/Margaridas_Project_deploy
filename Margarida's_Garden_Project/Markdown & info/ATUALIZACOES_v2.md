# 📝 Margarida's Garden & Treasury - Altualizações v2.0

## ✨ O Que Foi Adicionado

### 1. **Página Intermediária (Dashboard)**
- Localização: `/dashboard`
- Uma página elegante de seleção entre os dois aplicativos
- Design temático conforme o projeto
- Rápido acesso aos dois serviços:
  - **🌷 Margarida's Garden** - Gerenciador de senhas
  - **💎 Margarida's Treasury** - Gerenciador de finanças

### 2. **Margarida's Treasury - Novo Aplicativo de Finanças**

#### Funcionalidades Principais:

##### 📊 Gestão de Despesas
- Registrar despesas com:
  - **Nome**: Descrição da despesa
  - **Valor**: Montante gasto
  - **Data**: Data do gasto (padrão: hoje)
  - **Método**: Cartão, Dinheiro, Transferência, Débito, Pix, Boleto
  - **Notas**: Anotações opcionais
- Editar e deletar despesas
- Lista interativa com todas as despesas do usuário

##### 💰 Gestão de Receitas
- Registrar receitas com:
  - **Nome**: Descrição da receita
  - **Valor**: Montante recebido
  - **Data**: Data do recebimento (padrão: hoje)
  - **Notas**: Anotações opcionais
- Editar e deletar receitas
- Lista interativa com todas as receitas do usuário

##### 📈 Análises e Relatórios
- **Resumo Financeiro** com 3 períodos:
  - Últimos 3 meses
  - Últimos 6 meses
  - Últimos 12 meses
- **Métricas por período**:
  - Total de despesas
  - Total de receitas
  - Balanço (receitas - despesas)

##### 📊 Gráficos Visuais
1. **Gráfico de Métodos de Pagamento** (Tipo Doughnut)
   - Mostra distribuição de despesas por método
   - Mostra qual método é mais utilizado

2. **Gráfico Mensal** (Tipo Bar)
   - Comparação de despesas vs receitas
   - Últimos 12 meses
   - Visualização clara de tendências

## 🚀 Como Usar

### Fluxo de Login
1. Acesse a página inicial `/`
2. Clique em "Entrar"
3. Faça login com suas credenciais
4. **NOVO**: Será redirecionado para `/dashboard`
5. Escolha entre **Jardim de Senhas** ou **Tesouro Financeiro**

### Fluxo do Treasury
1. Clique em "Acessar Tesouro 💎"
2. **Aba Despesas**:
   - Preencha os dados e clique "Registrar Despesa"
   - Veja todas as despesas abaixo
   - Use ✏️ para editar ou 🗑️ para deletar
3. **Aba Receitas**:
   - Mesmo processo para receitas
4. **Aba Análises**:
   - Veja gráficos e resumos financeiros
   - Filtros por 3, 6 e 12 meses

## 📁 Arquivos Alterados e Adicionados

### Backend

#### Novos Modelos:
- `backend/app/models/expense.py` - Modelo de Despesa (com tipos de pagamento)
- `backend/app/models/income.py` - Modelo de Receita

#### Atualizado:
- `backend/app/models/user.py` - Adicionados relacionamentos com Expense e Income

#### Novos Schemas:
- `backend/app/schemas/expense.py` - Serialização de Despesa
- `backend/app/schemas/income.py` - Serialização de Receita

#### Novos Endpoints (API):
- `backend/app/api/treasury.py` - Todos os endpoints do Treasury:
  - `POST /api/treasury/expenses` - Criar despesa
  - `GET /api/treasury/expenses` - Listar despesas
  - `GET /api/treasury/expenses/{id}` - Obter despesa específica
  - `PUT /api/treasury/expenses/{id}` - Atualizar despesa
  - `DELETE /api/treasury/expenses/{id}` - Deletar despesa
  - `POST /api/treasury/incomes` - Criar receita
  - `GET /api/treasury/incomes` - Listar receitas
  - `GET /api/treasury/incomes/{id}` - Obter receita específica
  - `PUT /api/treasury/incomes/{id}` - Atualizar receita
  - `DELETE /api/treasury/incomes/{id}` - Deletar receita
  - `GET /api/treasury/analytics/summary` - Resumo financeiro
  - `GET /api/treasury/analytics/by-method` - Despesas por método
  - `GET /api/treasury/analytics/monthly` - Análise mensal

#### Atualizado:
- `backend/app/main.py` - Adicionadas rotas para `/dashboard` e `/treasury`, importação do novo router

#### Atualizado:
- `backend/app/models/__init__.py` - Importação dos novos modelos

### Frontend

#### Novas Páginas:
- `frontend/templates/dashboard.html` - Página de seleção entre aplicativos
- `frontend/templates/treasury.html` - Página principal do Treasury

#### Atualizado:
- `frontend/templates/login.html` - Redirecionamento alterado para `/dashboard`
- `frontend/static/css/style.css` - Adicionados estilos para dashboard e treasury
- `frontend/static/js/auth.js` - Função `apiRequest` corrigida para parseionar JSON

## 🎨 Design e Temas

- **Cores do Dashboard**: Mantém as cores do projeto (azul pastel, verde grama)
- **Cards Temáticos**:
  - Margarida's Garden: Verde (Grass Green)
  - Treasury: Amarelo (Flower Yellow)
- **Tipografia**: Consistente com o projeto (Segoe UI, Georgia)
- **Layout Responsivo**: Funciona em desktop e mobile

## 💾 Banco de Dados

Novas tabelas criadas automaticamente:
- `expenses` - Armazena despesas do usuário
- `incomes` - Armazena receitas do usuário

Campos da Tabela `expenses`:
- `id` (PK)
- `user_id` (FK)
- `name` (String)
- `value` (Float)
- `date` (DateTime)
- `method` (Enum: card, cash, transfer, debit, pix, bill)
- `notes` (String, nullable)
- `created_at`, `updated_at` (DateTime)

Campos da Tabela `incomes`:
- `id` (PK)
- `user_id` (FK)
- `name` (String)
- `value` (Float)
- `date` (DateTime)
- `notes` (String, nullable)
- `created_at`, `updated_at` (DateTime)

## 🔧 Instalação/Atualização

1. Reinicialize o banco de dados:
   ```bash
   python backend/scripts/init_db.py
   ```

2. As tabelas serão criadas automaticamente quando a aplicação inicia.

3. Execute a aplicação normalmente.

## 📊 Dependências

- **Chart.js** 3.9.1 - Para gráficos (importado via CDN)
- Nenhuma dependência Python nova foi adicionada

## 🐛 Notas Técnicas

- As datas padrão usam `datetime.now()` se não fornecidas
- Valores são validados para serem positivos
- Análises calculam períodos de forma dinâmica
- Gráficos são renderizados usando Chart.js
- Todos os endpoints requerem autenticação (JWT)

## 🎯 Próximas Melhorias Possíveis

- [ ] Exportar dados em CSV/PDF
- [ ] Categorias customizáveis para despesas
- [ ] Metas financeiras
- [ ] Notificações de despesas recorrentes
- [ ] Integração com e-mail para relatórios mensais
- [ ] Modo escuro
- [ ] Dashboard com widgets customizáveis

---

**Versão**: 2.0.0  
**Data**: Fevereiro 2026
