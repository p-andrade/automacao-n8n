# 04. Miniestudo Final — Da Intenção ao Workflow: Como Transformar Bons Prompts em Automações n8n

> **Navegação:** [⬅️ 03. Engenharia de Prompts](./03-engenharia-de-prompts.md) | [📚 Índice da Documentação](./README.md) | [Próximo: 05. Glossário ➡️](./05-glossario.md)

---

## 1. Introdução

O grande salto de maturidade para quem trabalha com automação de processos não está em decorar onde fica cada botão da interface gráfica do **n8n**, mas sim em saber **decompor um problema de negócio em etapas lógicas, contratos de dados e regras de exceção**.

Este miniestudo prático demonstra a jornada completa **da intenção ao workflow**: partindo de necessidades operacionais reais, estruturamos prompts de alta precisão e os traduzimos em dois workflows completos no n8n:
- **Cenário 01 (Determinístico):** Cadastro Automatizado de Leads (`workflows/01-cadastro-de-leads/`).
- **Cenário 02 (Cognitivo / Híbrido com IA):** Triagem Inteligente de Solicitações (`workflows/02-triagem-inteligente-ia/`).

---

## 2. Problema de Negócio

Operações digitais em crescimento sofrem com dois gargalos recorrentes na ponta de entrada de dados:

1. **Entrada Despadronizada de Leads Comerciais:** Formulários de páginas de captura (*landing pages*) enviam cadastros a qualquer hora do dia. Sem uma camada automatizada de validação e higienização, registros sem e-mail válido chegam ao time de vendas, nomes vêm desformatados e o tempo de resposta ao cliente ultrapassa horas.
2. **Sobrecarga na Triagem de Atendimento:** Caixas de entrada e formulários de contato recebem solicitações misturadas (pedidos de orçamento comercial, relatos de erro técnico urgente, dúvidas sobre boletos/faturas e mensagens aleatórias fora de escopo). A leitura manual atrasa o acionamento da equipe correta, especialmente em incidentes críticos.

---

## 3. Cenários Escolhidos

Para cobrir tanto a automação baseada em regras estritas quanto a automação apoiada por Inteligência Artificial Generativa, foram escolhidos dois cenários complementares:

| Atributo | Cenário 01: Cadastro Automatizado de Leads | Cenário 02: Triagem Inteligente com IA |
| :--- | :--- | :--- |
| **Natureza da Lógica** | 100% Determinística (Regras condicionais exatas). | Híbrida (Regras de validação + Classificação via IA + Guardrail determinístico). |
| **Entrada Principal** | Payload JSON com `nome`, `email`, `telefone`, `empresa`, `origem`. | Payload JSON com `solicitante`, `email`, `assunto`, `mensagem`, `prioridade_informada`. |
| **Processamento Central** | Higienização de strings, validação de obrigatoriedade/formato de e-mail e geração de protocolo de registro. | Limpeza de texto, verificação de mensagem, análise semântica por Agente de IA / Classificador e validação estrita do esquema de saída. |
| **Categorias / Saídas** | `200 OK` (Lead preparado e notificação demonstrativa gerada) ou `400 Bad Request` (Dados inválidos). | Classificação controlada em `Comercial`, `Suporte técnico`, `Financeiro` ou `Outros`, com prioridade e justificativa. |

---

## 4. Requisitos

### 4.1. Requisitos Funcionais (RF)
- **RF01 (Recepção HTTP):** Ambos os fluxos devem expor endpoints HTTP `POST` via nó `Webhook`.
- **RF02 (Higienização e Normalização):** Espaços em branco excedentes devem ser removidos (`.trim()`), e-mails convertidos para letras minúsculas (`.toLowerCase()`) e campos opcionais ausentes preenchidos com valores padrão seguros.
- **RF03 (Validação de Entrada):** Dados obrigatórios ausentes ou e-mails sem formato plausível devem ser barrados antes do processamento principal.
- **RF04 (Classificação Estruturada no Cenário 02):** Toda solicitação válida deve receber exatamente uma categoria permitida (`Comercial`, `Suporte técnico`, `Financeiro`, `Outros`), uma prioridade (`Alta`, `Média`, `Baixa`), um resumo objetivo e uma justificativa.
- **RF05 (Resposta Síncrona Demonstrativa):** Os workflows devem retornar o resultado processado diretamente no corpo da resposta HTTP (`Respond to Webhook`), permitindo inspeção completa sem exigir bancos de dados externos configurados.

### 4.2. Requisitos Não Funcionais (RNF)
- **RNF01 (Segurança e Privacidade):** Nenhuma chave de API, senha ou token real pode constar nos arquivos `workflow.json`.
- **RNF02 (Compatibilidade):** Uso exclusivo de nós nativos compatíveis com o n8n moderno (v1.x / v2.42.7).
- **RNF03 (Tolerância a Falhas):** O Cenário 02 deve garantir uma resposta estruturada válida mesmo que a saída da IA contenha variações ou esteja operando em modo demonstrativo local sem credenciais externas.

---

## 5. Construção do Prompt

Aplicando a metodologia documentada no [Capítulo 03](./03-engenharia-de-prompts.md), a construção dos prompts seguiu três etapas progressivas:

1. **Mapeamento da Intenção:** Definição clara de quem envia o dado, qual transformação ocorre e quem consome o resultado.
2. **Injeção de Regras e Restrições Técnicas:** Especificação dos nomes exatos dos nós (`Webhook Receber Lead`, `Validar Dados do Lead`, `Preparar Registro do Lead`, `Montar Notificacao Demonstrativa`, `Responder Sucesso`, `Responder Erro Validacao`), das condições booleanas e do bloqueio à sintaxe legada `$node[...]`.
3. **Padronização da Entrega:** Consolidação no arquivo principal [`prompts/prompt-final-desafio-dio.md`](../prompts/prompt-final-desafio-dio.md) e no template arquitetural [`prompts/prompt-design-workflow.md`](../prompts/prompt-design-workflow.md).

---

## 6. Arquitetura Proposta

### 6.1. Fluxo do Cenário 01 — Cadastro Automatizado de Leads
1. **`Webhook Receber Lead`** (`n8n-nodes-base.webhook`): Escuta `POST /cadastro-leads`.
2. **`Validar Dados do Lead`** (`n8n-nodes-base.if`): Verifica se `nome` não está vazio e se `email` contém `@` e `.`.
   - **Caminho Verdadeiro (`true`):** Segue para **`Preparar Registro do Lead`**.
   - **Caminho Falso (`false`):** Desvia imediatamente para **`Responder Erro Validacao`** (HTTP 400).
3. **`Preparar Registro do Lead`** (`n8n-nodes-base.set`): Normaliza `nome`, `email`, `telefone`, `empresa`, `origem`, gera `lead_id` demonstrativo e `data_processamento`.
4. **`Montar Notificacao Demonstrativa`** (`n8n-nodes-base.set`): Constrói a mensagem estruturada que seria enviada para um canal comercial e empacota o status `registrado_demonstrativo`.
5. **`Responder Sucesso`** (`n8n-nodes-base.respondToWebhook`): Retorna HTTP `200 OK` com os dados higienizados e o resumo da notificação.

### 6.2. Fluxo do Cenário 02 — Triagem Inteligente com IA
1. **`Webhook Entrada Solicitacao`** (`n8n-nodes-base.webhook`): Escuta `POST /triagem-ia`.
2. **`Normalizar Dados de Entrada`** (`n8n-nodes-base.set`): Extrai e limpa `solicitante`, `email`, `assunto`, `mensagem` e `prioridade_informada`.
3. **`Verificar Dados Obrigatorios`** (`n8n-nodes-base.if`): Confirma se `solicitante`, `email` válido e `mensagem` (com conteúdo mínimo) estão presentes.
   - **Caminho Falso (`false`):** Desvia para **`Responder Erro Dados Incompletos`** (HTTP 400).
4. **`Agente IA de Triagem`** (`@n8n/n8n-nodes-langchain.agent`) conectado ao sub-nó **`Modelo OpenAI Chat`** (`@n8n/n8n-nodes-langchain.lmChatOpenAi`): Recebe o texto normalizado e as instruções de sistema para classificar em JSON (`categoria`, `prioridade`, `resumo`, `justificativa`). Configurado com `continueOnFail: true` para permitir resiliência caso não haja credencial ativa no ambiente de teste.
5. **`Validar e Classificar Resposta`** (`n8n-nodes-base.code`): Nó de *guardrail* e validação pós-IA. Verifica se o `Agente IA de Triagem` retornou um JSON válido dentro das categorias permitidas (`Comercial`, `Suporte técnico`, `Financeiro`, `Outros`) e prioridades permitidas (`Alta`, `Média`, `Baixa`). Caso a resposta da IA seja inválida ou caso o fluxo esteja rodando em modo demonstrativo sem credencial da OpenAI, aplica uma regra determinística transparente (`modo_execucao: "fallback_demonstrativo_regras"` vs `"ia_validada"`), garantindo que o fluxo nunca quebre.
6. **`Formatar Saida Estruturada`** (`n8n-nodes-base.set`): Padroniza o envelope final de retorno.
7. **`Responder Triagem Concluida`** (`n8n-nodes-base.respondToWebhook`): Retorna HTTP `200 OK` com a classificação auditada.

---

## 7. Seleção dos Nós

A tabela abaixo justifica tecnicamente a escolha de cada tipo de nó nativo do n8n:

| Nó Escolhido | Tipo Técnico no n8n | Justificativa de Arquitetura |
| :--- | :--- | :--- |
| **Webhook** | `n8n-nodes-base.webhook` | Padrão universal para integração orientada a eventos via HTTP, suportando qualquer linguagem ou formulário frontend. |
| **IF** | `n8n-nodes-base.if` | Permite implementar o padrão *Fail-Fast* visualmente, separando o caminho feliz (*happy path*) do tratamento de erros. |
| **Edit Fields (Set)** | `n8n-nodes-base.set` | Ideal para mapear, limpar e tipar propriedades JSON de forma declarativa e legível sem necessidade de scripts complexos. |
| **AI Agent + OpenAI Chat Model** | `@n8n/n8n-nodes-langchain.agent` + `lmChatOpenAi` | Arquitetura moderna de *Cluster Nodes* do n8n para raciocínio sobre texto não estruturado com instruções de sistema (*System Prompt*). |
| **Code (JavaScript)** | `n8n-nodes-base.code` | Utilizado no Cenário 02 para parsing seguro (`JSON.parse` com `try/catch`), validação estrita de domínio (*enum check*) e fallback determinístico. |
| **Respond to Webhook** | `n8n-nodes-base.respondToWebhook` | Permite devolver códigos HTTP semânticos (`200` vs `400`) e payloads JSON ricos diretamente ao cliente chamador. |

---

## 8. Implementação Demonstrativa

Os dois workflows foram implementados integralmente nos diretórios:
- [`workflows/01-cadastro-de-leads/workflow.json`](../workflows/01-cadastro-de-leads/workflow.json)
- [`workflows/02-triagem-inteligente-ia/workflow.json`](../workflows/02-triagem-inteligente-ia/workflow.json)

> [!NOTE]
> **Transparência sobre Persistência e Integrações Externas:**
> Em estrita conformidade com as regras de execução do projeto, **nenhum serviço externo dependente de credenciais privadas foi acoplado como requisito bloqueante**, e **não afirmamos que leads foram gravados em um banco de dados externo real**. Em vez disso, os workflows implementam saídas demonstrativas completas que preparam o objeto exato de registro/notificação e o retornam via `Respond to Webhook`.

---

## 9. Testes

A estratégia de testes combinou duas frentes complementares:
1. **Validação Estrutural e Estática Executada Localmente:** O script [`tests/validar-workflows.py`](../tests/validar-workflows.py) foi executado com Python `3.15.0` no ambiente de desenvolvimento, inspecionando os dois arquivos `workflow.json` e os quatro arquivos JSON de payloads de exemplo.
2. **Simulação Lógica e Casos de Teste Documentados:** Em [`tests/casos-de-teste.md`](../tests/casos-de-teste.md), foram definidos 10 casos de teste cobrindo payloads válidos, campos obrigatórios ausentes, e-mails malformados e mensagens fora de escopo.

---

## 10. Resultados Efetivamente Observados

- **Validação dos Arquivos JSON (`validar-workflows.py`):** **100% de aprovação**. Os dois workflows e todos os exemplos de payload são sintaticamente válidos, possuem todos os nós e conexões íntegros, não apresentam nomes de nós duplicados e não contêm nenhum segredo ou credencial exposta.
- **Verificação do Ambiente n8n:** Foi constatada a presença do binário `n8n` versão `2.42.7` no ambiente local. Contudo, como não havia um servidor n8n ativo com credenciais da OpenAI configuradas durante a sessão automatizada, as validações de estrutura de grafo e contrato JSON foram executadas estaticamente via Python, enquanto os testes de disparo HTTP ao vivo contra o motor de IA foram devidamente classificados no relatório de testes como **dependentes de importação e configuração de credencial pelo usuário**.

---

## 11. Limitações

1. **Dependência de Credencial para IA Real no Workflow 02:** Para que o nó `Agente IA de Triagem` consulte a API da OpenAI em tempo real, o usuário que importar o fluxo precisará cadastrar sua própria credencial `OpenAI API` no painel do n8n. Sem ela, o fluxo opera através do caminho de contingência demonstrativo implementado no nó `Validar e Classificar Resposta`.
2. **Ausência de Persistência em Banco de Dados:** O Workflow 01 prepara o payload higienizado e retorna confirmação HTTP, mas não grava em PostgreSQL/Google Sheets por padrão para manter o template 100% portátil e livre de configurações externas obrigatórias.
3. **Validação de E-mail Sintática:** A verificação no nó `IF` checa a presença de caracteres estruturais (`@` e `.`), mas não verifica a existência real da caixa postal via registros DNS MX.

---

## 12. Melhorias Futuras

1. **Persistência Idempotente (PostgreSQL / Supabase):** Adicionar um nó de banco de dados após `Preparar Registro do Lead` utilizando a operação `Upsert` com `email` como chave única para evitar duplicidade.
2. **Autenticação no Webhook:** Habilitar `Header Auth` nos nós `Webhook` em ambiente produtivo para exigir um token seguro nas requisições recebidas.
3. **Sub-workflow Global de Erros (`Error Trigger`):** Conectar ambos os fluxos a um workflow central de observabilidade para alertar administradores caso ocorram indisponibilidades de infraestrutura.

---

## 13. Conclusão

Este miniestudo comprova que **bons prompts são a ponte entre a necessidade humana e a automação confiável**. Quando especificamos persona, contexto, sequência de nós, regras de negócio, restrições de versão e tratamento de exceções antes de construir o workflow, transformamos a Inteligência Artificial em uma verdadeira parceira de engenharia de software — capaz de acelerar a criação de fluxos modulares, seguros, documentados e fáceis de manter no n8n.
