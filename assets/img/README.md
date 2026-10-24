# 🖼️ Catálogo de Imagens Didáticas (`assets/img/`)

> **Navegação:** [⬅️ Diretório `assets/`](../README.md) | [🏠 README Principal](../../README.md) | [⚙️ Workflows n8n](../../workflows/README.md)

---

## 📌 Especificações Técnicas das Imagens

Todas as **15 imagens** deste diretório foram produzidas no formato **PNG (`1400x780` pixels, proporção horizontal `16:9`)**, com paleta escura de alto contraste (*Dark Tech Theme*), tipografia legível e nomenclatura fiel aos nós dos arquivos `workflow.json`.

> [!NOTE]
> **Nota de Transparência Visual:** As imagens abaixo são **diagramas técnicos esquemáticos didáticos** criados especificamente para explicar a entrada, a regra de negócio, a saída e o tratamento de erro de cada nó do n8n para estudantes e iniciantes. Elas não são apresentadas como capturas de tela falsas da interface proprietária.

---

## 🗂️ Inventário Completo das 15 Imagens

### 1. Identidade e Arquitetura Geral (`assets/img/`)
| Arquivo | Dimensões | Finalidade Didática | Onde é Utilizada |
| :--- | :---: | :--- | :--- |
| [`banner-projeto.png`](./banner-projeto.png) | `1400x780` | Banner oficial de abertura com título do projeto, referência ao Desafio DIO, n8n e pipeline de 4 etapas. | Topo do [`README.md`](../../README.md) principal. |
| [`arquitetura-geral.png`](./arquitetura-geral.png) | `1400x780` | Demonstra como uma necessidade de negócio vira prompt, arquitetura, workflow JSON e testes. | [`README.md`](../../README.md) e [`docs/06-arquitetura-da-solucao.md`](../../docs/06-arquitetura-da-solucao.md). |

---

### 2. Workflow 01 — Cadastro Automatizado de Leads (`assets/img/01-cadastro-leads/`)
| Arquivo | Nó(s) Documentado(s) | Finalidade Didática |
| :--- | :--- | :--- |
| [`01-visao-geral.png`](./01-cadastro-leads/01-visao-geral.png) | Todos os 6 nós do Workflow 01 | Visão panorâmica do fluxo completo e da separação entre caminho válido (`True`) e erro (`False`). |
| [`02-no-webhook.png`](./01-cadastro-leads/02-no-webhook.png) | `Webhook Receber Lead` | Explica a recepção HTTP `POST /cadastro-leads` e o payload bruto de entrada. |
| [`03-no-validacao.png`](./01-cadastro-leads/03-no-validacao.png) | `Validar Dados do Lead` | Detalha as 3 condições `AND` (nome preenchido + e-mail com `@` e `.`) e o desvio de erro. |
| [`04-no-registro.png`](./01-cadastro-leads/04-no-registro.png) | `Preparar Registro do Lead` | Mostra a higienização (`.trim()`, `.toLowerCase()`), valores padrão e geração de `lead_id`. |
| [`05-no-notificacao.png`](./01-cadastro-leads/05-no-notificacao.png) | `Montar Notificacao Demonstrativa` + `Responder Sucesso` | Demonstra a montagem da resposta estruturada e o aviso transparente de saída demonstrativa. |
| [`06-fluxo-completo.png`](./01-cadastro-leads/06-fluxo-completo.png) | Arquitetura completa (6 nós) | Mapa final consolidando nós, tipos, conexões e portas `HTTP 200` vs `HTTP 400`. |

---

### 3. Workflow 02 — Triagem Inteligente com IA (`assets/img/02-triagem-inteligente-ia/`)
| Arquivo | Nó(s) Documentado(s) | Finalidade Didática |
| :--- | :--- | :--- |
| [`01-visao-geral.png`](./02-triagem-inteligente-ia/01-visao-geral.png) | Todos os 8 nós do Workflow 02 | Visão panorâmica da triagem inteligente desde a entrada até a resposta validada. |
| [`02-no-entrada.png`](./02-triagem-inteligente-ia/02-no-entrada.png) | `Webhook Entrada Solicitacao` | Explica o recebimento da solicitação em `POST /triagem-ia`. |
| [`03-no-normalizacao.png`](./02-triagem-inteligente-ia/03-no-normalizacao.png) | `Normalizar Dados de Entrada` + `Verificar Dados Obrigatorios` | Mostra a limpeza dos campos e o bloqueio de chamados sem mensagem ou sem e-mail válido. |
| [`04-no-agente-ia.png`](./02-triagem-inteligente-ia/04-no-agente-ia.png) | `Agente IA de Triagem` + `Modelo OpenAI Chat` | Detalha o prompt de sistema, o modelo `gpt-4o-mini` e o formato JSON esperado da IA. |
| [`05-no-classificacao.png`](./02-triagem-inteligente-ia/05-no-classificacao.png) | `Validar e Classificar Resposta` | Explica o *Guardrail* em JavaScript que valida categorias/prioridades e aplica fallback seguro. |
| [`06-no-saida.png`](./02-triagem-inteligente-ia/06-no-saida.png) | `Formatar Saida Estruturada` + `Responder Triagem Concluida` | Apresenta o contrato JSON final retornado ao solicitante (`HTTP 200 OK`). |
| [`07-fluxo-completo.png`](./02-triagem-inteligente-ia/07-fluxo-completo.png) | Arquitetura completa (8 nós) | Diagrama final incluindo a conexão `ai_languageModel` do sub-nó e os tratamentos de erro. |
