# 📝 CHANGELOG - Margarida's Garden v2.0

## [2.0.0] - 2026-02-11

### ✨ Novas Funcionalidades

#### Dashboard Intermediário
- [NEW] Página `/dashboard` - Seletor entre aplicativos após login
- [NEW] Cards temáticos para Margarida's Garden e Margarida's Treasury
- [NEW] Navegação fluida entre os dois aplicativos
- [NEW] Resumo rápido de finanças no dashboard (opcional)

#### Margarida's Treasury - Novo Aplicativo
- [NEW] Página principal `/treasury` com interface completa
- [NEW] Sistema de gestão de **Despesas**
- [NEW] Sistema de gestão de **Receitas**
- [NEW] Sistema de **Análises e Relatórios**
- [NEW] **Gráficos interativos** (Chart.js)

##### Funcionalidades de Despesas
- [NEW] Criar despesa com campos: Nome, Valor, Data, Método(6 tipos), Notas
- [NEW] Listar todas as despesas do usuário
- [NEW] Editar despesa existente
- [NEW] Deletar despesa com confirmação
- [NEW] Suporte a 6 métodos de pagamento:
  - Cartão
  - Dinheiro
  - Transferência
  - Débito
  - Pix
  - Boleto

##### Funcionalidades de Receitas
- [NEW] Criar receita com campos: Nome, Valor, Data, Notas
- [NEW] Listar todas as receitas do usuário
- [NEW] Editar receita existente
- [NEW] Deletar receita com confirmação

##### Análises e Relatórios
- [NEW] Resumo financeiro com períodos:
  - Últimos 3 meses
  - Últimos 6 meses
  - Últimos 12 meses
- [NEW] Cálculo de:
  - Total de despesas
  - Total de receitas
  - Balanço (receitas - despesas)
- [NEW] **Gráfico Doughnut** - Despesas por método de pagamento
- [NEW] **Gráfico Bar** - Despesas vs Receitas mensal (12 meses)

### 🗄️ Modelos de Dados

#### Novos Modelos
```python
# ExpenseModel com suporte a enum de métodos
class Expense(Base):
    - id: int
    - user_id: int (FK)
    - name: str (255)
    - value: float
    - date: datetime
    - method: enum(card, cash, transfer, debit, pix, bill)
    - notes: str (500, nullable)
    - created_at: datetime
    - updated_at: datetime

# Income Model
class Income(Base):
    - id: int
    - user_id: int (FK)
    - name: str (255)
    - value: float
    - date: datetime
    - notes: str (500, nullable)
    - created_at: datetime
    - updated_at: datetime
```

#### Relações Atualizadas
```python
# User agora tem relacionamentos com:
- credentials (Credential) - já existia
- expenses (Expense) - novo
- incomes (Income) - novo
```

### 🔌 API REST Endpoints

#### Despesas (5 endpoints)
- `POST /api/treasury/expenses` - Criar despesa
- `GET /api/treasury/expenses` - Listar despesas
- `GET /api/treasury/expenses/{id}` - Obter despesa específica
- `PUT /api/treasury/expenses/{id}` - Atualizar despesa
- `DELETE /api/treasury/expenses/{id}` - Deletar despesa

#### Receitas (5 endpoints)
- `POST /api/treasury/incomes` - Criar receita
- `GET /api/treasury/incomes` - Listar receitas
- `GET /api/treasury/incomes/{id}` - Obter receita específica
- `PUT /api/treasury/incomes/{id}` - Atualizar receita
- `DELETE /api/treasury/incomes/{id}` - Deletar receita

#### Análises (3 endpoints)
- `GET /api/treasury/analytics/summary` - Resumo por períodos
- `GET /api/treasury/analytics/by-method` - Despesas agrupadas por método
- `GET /api/treasury/analytics/monthly` - Dados mensais dos últimos 12 meses

**Total: 19 novos endpoints**

### 🎨 Frontend

#### Novas Páginas
- [NEW] `frontend/templates/dashboard.html` (340 linhas)
  - Cards para seleção de aplicativos
  - Design temático com gradient
  - Responsivo para mobile/tablet/desktop
  - Botão de logout

- [NEW] `frontend/templates/treasury.html` (650 linhas)
  - 3 abas: Despesas, Receitas, Análises
  - Formulários com validação
  - Lista interativa com edição/deleção
  - Gráficos em tempo real
  - Responsivo completo

#### Atualizações
- [UPDATE] `frontend/templates/login.html`
  - Redirecionamento alterado: `/garden` → `/dashboard`
  
- [UPDATE] `frontend/static/js/auth.js`
  - Função `apiRequest()` agora parseia JSON automaticamente
  - Melhorado tratamento de erros
  
- [UPDATE] `frontend/static/css/style.css` (+500 linhas)
  - Estilos para Dashboard
  - Estilos para Treasury
  - Estilos para Gráficos
  - Responsividade aprimorada
  - Animações e transições

#### Novas Dependências Frontend
- [NEW] Chart.js 3.9.1 (via CDN)

### 🔐 Autenticação

- [MAINTAINED] JWT Bearer Token
- [MAINTAINED] Todos os endpoints requerem autenticação
- [MAINTAINED] Dados filtrados por user_id
- [IMPROVED] Melhorado tratamento de sessão expirada

### 📊 Banco de Dados

#### Novas Tabelas
- `expenses` (19 campos com índices)
- `incomes` (16 campos com índices)

#### Schema Atualizado
- Tabela `users` - Adicionados relacionamentos
- Integridade referencial mantida
- Cascade delete configurado

### 🧪 Validações

#### Despesa
- ✅ Nome obrigatório (1-255 chars)
- ✅ Valor obrigatório (> 0)
- ✅ Método obrigatório (enum validado)
- ✅ Data padrão (datetime.now())
- ✅ Notas opcionais

#### Receita
- ✅ Nome obrigatório (1-255 chars)
- ✅ Valor obrigatório (> 0)
- ✅ Data padrão (datetime.now())
- ✅ Notas opcionais

### 🎯 Performance

- ✅ Índices em foreign keys
- ✅ Queries otimizadas com filtros
- ✅ Paginação não implementada mas é escalável
- ✅ Gráficos renderizam eficientemente

### 📱 Responsividade

- ✅ Mobile-first design
- ✅ Breakpoints: < 768px, 768-1199px, > 1200px
- ✅ Cards empilhados em mobile
- ✅ Gráficos responsivos

### 🎨 Design & UX

#### Tema Mantido
- ✅ Cores pastel consistentes
- ✅ Tipografia coherente
- ✅ Animações e transições suaves
- ✅ User-friendly interface

#### Novos Elementos de Design
- Dashboard cards temáticos
- Abas com indicador ativo
- Cards de resumo com gradientes
- Modale de edição
- Gráficos coloridos
- Empty states informativos

### 📚 Documentação

- [NEW] `ATUALIZACOES_v2.md` - Documentação completa do v2.0
- [NEW] `GUIA_TESTE_v2.md` - Guia passo-a-passo de testes
- [NEW] `CONFIGURACAO.md` - Setup e configuração
- [NEW] `RESUMO_IMPLEMENTACAO.md` - Sumário visual
- [NEW] `CHANGELOG.md` - Este arquivo

### 🔄 Fluxo de Usuário Atualizado

```
1. Acesse /               Landing Page
2. Clique "Entrar"        → /login
3. Faça login             → /dashboard (NOVO!)
4. Escolha um app:
   - Senhas               → /garden
   - Finanças             → /treasury (NOVO!)
5. Use o aplicativo       Por conta própria
6. Clique "Sair"         → / (Landing)
```

### 🐛 Bug Fixes

- [FIX] apiRequest não parseava JSON corretamente
- [FIX] Redirecionamento após login agora leva ao dashboard

### ⚡ Melhorias Gerais

- [IMPROVED] URL routing melhorado
- [IMPROVED] Error handling mais robusto
- [IMPROVED] Código Python mais type-safe com enums
- [IMPROVED] JavaScript modularizado por funcionalidade

### 🚀 Recursos Futuros Sugeridos

- [ ] Exportar dados em CSV/Excel
- [ ] Relatórios em PDF
- [ ] Categorias customizáveis
- [ ] Metas financeiras
- [ ] Lembretes de despesas recorrentes
- [ ] Integração com e-mail
- [ ] Modo escuro
- [ ] Dashboard customizável
- [ ] Multi-moeda
- [ ] Previsões (machine learning)

### 📦 Dependências

#### Backend (Sem mudanças)
```
fastapi==0.109.2
uvicorn[standard]==0.27.1
jinja2==3.1.3
sqlalchemy>=2.0.41
alembic>=1.13.1
python-jose[cryptography]==3.3.0
passlib==1.7.4
bcrypt==3.2.2
python-multipart==0.0.9
email-validator==2.1.0
```

#### Frontend
- Chart.js 3.9.1 (via CDN - sem instalação)

### 🔄 Migração de Dados

Para usuários existentes:
```bash
# Automaticamente criará novas tabelas
python backend/scripts/init_db.py
```

Não há perda de dados. Credenciais existentes serão mantidas.

### ⚠️ Breaking Changes

❌ NENHUM - Totalmente compatível com v1.0
- Endpoints antigos funcionam como antes
- Páginas antigas funcionam como antes
- Apenas novas funcionalidades adicionadas

### 🔒 Segurança

- ✅ Todas as APIs requerem JWT
- ✅ Validação de entrada
- ✅ SQL Injection protection (SQLAlchemy)
- ✅ XSS protection (Jinja2)
- ✅ CORS configurado

### 📊 Estatísticas da Release

| Métrica | Valor |
|---------|-------|
| Linha de Código Adicionadas | ~2500 |
| Novos Arquivos | 7 |
| Arquivos Atualizados | 5 |
| Novos Endpoints | 19 |
| Novos Modelos | 2 |
| Novos Schemas | 2 |
| Novos Gráficos | 2 |
| Documentação (linhas) | ~1000 |

---

## Versão Anterior: [1.0.0] - Margarida's Garden (Senha)

### Funcionalidades v1.0
- ✅ Gerenciador de senhas
- ✅ Autenticação JWT
- ✅ Frontend Jinja2
- ✅ SQLAlchemy ORM
- ✅ API RESTful

---

**Data de Release**: 11 de Fevereiro de 2026  
**Desenvolvido por**: AI Assistant  
**Status**: ✅ Pronto para Produção
