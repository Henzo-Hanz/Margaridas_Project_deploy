# Plano do Projeto — Margarida's Garden

## Visão Geral

**Objetivo:** Desenvolver um gerenciador de senhas amigável, seguro e confiável, com UI intuitiva e bonita.

**Stack principal:** Python, FastAPI (Backend Web), Flutter/Web para interface (comando `void main() => runApp(WebApp());` para abrir em navegador, sem necessidade de builds mobile específicos).

**Contexto:** Projeto educacional para familiarização com a IDE Cursor e uso de agentes de IA (GPT-Codex, Sonnet 4.5, Compose 1.0, etc.) no desenvolvimento.

---

## Fases do Projeto

### Fase 1 — Fundação e Backend (Prioridade Alta)

#### 1.1 Definição do Banco de Dados
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.1.1 | Escolher e documentar o SGBD (SQLite para local, PostgreSQL para produção) | Documento de decisão técnica |
| 1.1.2 | Definir ORM — **SQLAlchemy** | Configuração inicial do projeto |
| 1.1.3 | Avaliar desempenho e segurança; implementar testes unitários | Suite de testes e relatório |

#### 1.2 Modelagem e Estrutura do Banco
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.2.1 | Modelar banco de dados e relacionamentos (BRModelo ou similar) | Diagrama ER / modelo conceitual |
| 1.2.2 | Configurar **Alembic** para versionamento e migrações (evitar SQL direto) | Estrutura de migrações |
| 1.2.3 | Criar models iniciais (ex.: `User`, `Password`, `Credential`) | Models SQLAlchemy |
| 1.2.4 | Criar model de teste e validar migrações | Migração inicial funcional |

#### 1.3 Autenticação e Segurança
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.3.1 | Implementar **FastAPI OAuth2** para autenticação | Endpoints de login/logout |
| 1.3.2 | Avaliar **InstantDB Magic number auth** como alternativa | Documento de comparação |
| 1.3.3 | Implementar autenticação interna e geração de tokens | Sistema de tokens JWT ou similar |

#### 1.4 API e Operações CRUD
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.4.1 | Endpoints para **adicionar** senhas (DML) | `POST /passwords` |
| 1.4.2 | Endpoints para **editar** senhas | `PUT /passwords/{id}` |
| 1.4.3 | Endpoints para **apagar** senhas | `DELETE /passwords/{id}` |
| 1.4.4 | Endpoints para **listar** senhas (com criptografia adequada) | `GET /passwords` |
| 1.4.5 | Armazenamento seguro (hash, salt, criptografia) | Implementação validada |

#### 1.5 Permissões e Gerenciamento
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.5.1 | Definir modelo de permissões de usuário | Documento de permissões |
| 1.5.2 | Implementar controle de acesso por usuário | Middleware/Depends no FastAPI |

#### 1.6 Debugging, Segurança e Rastreamento
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 1.6.1 | Configurar logging e rastreamento de erros | Logs estruturados |
| 1.6.2 | Revisão de segurança (OWASP, injeção, etc.) | Checklist de segurança |

---

### Fase 2 — Layout e Estilo (Paralelo / Após Fase 1)

#### 2.1 Estrutura da Landing Page
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 2.1.1 | **Separar componentes** da landing page em módulos reutilizáveis | Estrutura de componentes |
| 2.1.2 | Definir paleta (fundo branco ou azul, chão verde) | Guia de estilo |

#### 2.2 Elementos Visuais
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 2.2.1 | Implementar saudação centralizada: "Olá [Nome], seja bem-vinda ao seu jardim de senhas!" | Componente de saudação |
| 2.2.2 | V1: suporte a 1 usuário fixo; preparar para multi-usuário futuro | Lógica de nome dinâmico |
| 2.2.3 | Criar "chão" verde e flores de cores variadas (aleatórias ou fixas) | Assets e CSS/Canvas |

#### 2.3 Animações
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 2.3.1 | Animação de flores balançando | Animação CSS/JS |
| 2.3.2 | Ao fim do ciclo: pétala se solta e sobe | Animação de pétala |
| 2.3.3 | Pétala: torna-se branca, mais arredondada durante subida | Transição visual |
| 2.3.4 | Exibir strings com aparência de encriptação/salt (ex.: `sy$gu89&87eudeu873j@hdj`) no centro da pétala | Overlay de texto |
| 2.3.5 | Pétala some ao atingir altura máxima da janela | Fade out / remoção |

---

### Fase 3 — Frontend e Integração

#### 3.1 Consumo da API
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 3.1.1 | Integrar frontend com endpoints do backend | Cliente HTTP configurado |
| 3.1.2 | Enviar dados via forms para a API | Formulários funcionais |
| 3.1.3 | Usar templates HTML da pasta `templates` (sem React obrigatório) | Estrutura de templates |

#### 3.2 Homepage e UI
| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 3.2.1 | **Implementar o estilo do layout na homepage ("/")** | Homepage completa |
| 3.2.2 | UI amigável e simplificada para CRUD de senhas | Telas de listagem, criação, edição e exclusão |

---

### Fase 4 — Deploy e Infraestrutura

| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 4.1 | Avaliar e documentar opções: **AWS**, **Vercel**, **Servidor próprio** | Documento de deploy |
| 4.2 | Implementar deploy em ambiente escolhido | Aplicação em produção |

---

### Fase 5 — Backups (Plano à Parte — Opcional)

| Tarefa | Descrição | Entregável |
|--------|-----------|------------|
| 5.1 | Priorizar banco de dados local na implementação principal | — |
| 5.2 | Plano de implementação separado para backups (nuvem, WhatsApp, Discord, Drive, etc.) | Documento de requisitos |
| 5.3 | Garantir segurança dos dados em backups | Criptografia e políticas |

---

## Ordem Sugerida de Implementação

```
1. Backend (DB + Models + API + Auth)
2. Layout/Estilo (componentes + animações)
3. Frontend (templates + integração)
4. Deploy
5. Backups (opcional)
```

---

## Estrutura de Pastas Sugerida

```
Margarida's_Garden_Project/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── api/
│   │   ├── core/
│   │   └── ...
│   ├── alembic/
│   └── tests/
├── frontend/
│   ├── templates/
│   ├── static/
│   └── ...
├── Ideias_iniciais.md
└── Plano_do_Projeto.md
```

---

## Critérios de Conclusão por Fase

- **Fase 1:** API funcional, autenticada, com CRUD de senhas e testes passando.
- **Fase 2:** Landing page com animações e saudação conforme especificado.
- **Fase 3:** Usuário consegue gerenciar senhas pela interface.
- **Fase 4:** Aplicação acessível em ambiente de produção.
- **Fase 5:** Backups opcionais documentados e, se implementados, seguros.
