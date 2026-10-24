# 02. Curadoria de Fontes e Referências Oficiais

> **Navegação:** [⬅️ 01. Contexto e Objetivos](./01-contexto-e-objetivos.md) | [📚 Índice da Documentação](./README.md) | [Próximo: 03. Engenharia de Prompts ➡️](./03-engenharia-de-prompts.md)

---

## 1. Metodologia de Pesquisa e Seleção de Fontes

Para garantir que os prompts, workflows e diagramas deste projeto reflitam o comportamento real do **n8n** (versão instalada `2.42.7` verificada no ambiente local) e as boas práticas do **GitHub**, adotou-se um protocolo estrito de curadoria baseado na distinção entre **Fontes Primárias** e **Fontes Secundárias**.

### 1.1. Fontes Primárias vs. Fontes Secundárias

| Classificação | Definição Técnica | Exemplos no Ecossistema n8n / IA | Papel neste Projeto |
| :--- | :--- | :--- | :--- |
| **Fontes Primárias** | Documentação técnica oficial, código-fonte original, especificações de API e manuais mantidos diretamente pelos fabricantes ou criadores da tecnologia. | `docs.n8n.io`, repositório `github.com/n8n-io/n8n`, `docs.github.com`. | **Autoridade normativa (Fonte da Verdade):** Utilizadas obrigatoriamente para definir tipos de nós, parâmetros JSON, sintaxe de expressões e comandos CLI. |
| **Fontes Secundárias** | Materiais interpretativos ou derivados criados por terceiros, como tutoriais em blogs, vídeos, fóruns de discussão ou sínteses geradas por LLMs sem ancoragem documental. | Tutoriais antigos no Medium/YouTube, respostas de modelos de IA baseadas apenas em memória de treinamento. | **Apoio conceitual sujeito a auditoria:** Nunca são aceitas sem verificação cruzada na fonte primária, pois frequentemente contêm sintaxes depreciadas (como `$node["Nome"]` da versão 0.x). |

### 1.2. Critérios de Seleção Aplicados

1. **Autoridade Institucional:** Prioridade absoluta às páginas sob os domínios oficiais `docs.n8n.io`, `github.com/n8n-io/n8n` e `docs.github.com`.
2. **Acurácia de Versão:** Conformidade com a estrutura de dados em *item-lists*, expressões modernas (`$json`, `$('Nome do Nó').item.json`) e nós nativos atuais (`Webhook`, `IF`, `Edit Fields (Set)`, `Respond to Webhook`, `Code` e `AI Agent`).
3. **Verificabilidade Empírica:** Todas as URLs listadas abaixo foram efetivamente consultadas e verificadas durante a execução do projeto em **24/10/2026**. Nenhuma fonte, data ou funcionalidade foi inventada.

---

## 2. Registro Auditável das Páginas Consultadas

A tabela sintética a seguir consolida todas as páginas oficiais inspecionadas diretamente no ambiente durante o desenvolvimento deste projeto:

| # | Título Oficial da Página | URL Consultada | Organização | Finalidade da Consulta no Projeto | Data de Acesso |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **01** | *n8n Documentation — Welcome to n8n Docs* | https://docs.n8n.io/ | n8n GmbH | Visão geral da arquitetura da plataforma, categorias de nós e estrutura da documentação oficial. | 24/10/2026 |
| **02** | *Workflows — Core Concepts and Data Flow* | https://docs.n8n.io/workflows/ | n8n GmbH | Fundamentação sobre criação de workflows, estrutura JSON exportável, conexões e fluxo de itens. | 24/10/2026 |
| **03** | *Webhook Node Documentation* | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ | n8n GmbH | Especificação do nó `n8n-nodes-base.webhook`, métodos HTTP (`POST`), `responseMode` e separação entre URLs de teste e produção. | 24/10/2026 |
| **04** | *If Node Documentation* | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/ | n8n GmbH | Configuração do nó condicional `n8n-nodes-base.if`, operadores de validação booleana/string e roteamento *true/false*. | 24/10/2026 |
| **05** | *Edit Fields (Set) Node Documentation* | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/ | n8n GmbH | Uso do nó `n8n-nodes-base.set` (renomeado na interface moderna para *Edit Fields (Set)*) para normalizar e estruturar campos JSON. | 24/10/2026 |
| **06** | *Respond to Webhook Node Documentation* | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/ | n8n GmbH | Configuração de respostas HTTP síncronas customizadas (códigos `200`, `400`, `422`) com corpo JSON estruturado. | 24/10/2026 |
| **07** | *Advanced AI in n8n (LangChain Integration)* | https://docs.n8n.io/advanced-ai/ | n8n GmbH | Arquitetura de nós de Inteligência Artificial no n8n, conceito de *Cluster Nodes* (nó raiz + sub-nós de modelo, memória e tools). | 24/10/2026 |
| **08** | *AI Agent Node Documentation* | https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/ | n8n GmbH | Parametrização do nó `@n8n/n8n-nodes-langchain.agent`, definição de *System Message / Prompt* e controle de saída no Workflow 02. | 24/10/2026 |
| **09** | *n8n Official GitHub Repository* | https://github.com/n8n-io/n8n | n8n GmbH | Código-fonte oficial do n8n, licença *Sustainable Use License*, pacotes internos (`n8n-nodes-base`, `@n8n/n8n-nodes-langchain`) e CLI. | 24/10/2026 |
| **10** | *Sobre Repositórios — Documentação do GitHub* | https://docs.github.com/pt/repositories/creating-and-managing-repositories/about-repositories | GitHub, Inc. | Boas práticas de organização de repositórios públicos, visibilidade, arquivo `README.md`, licenciamento e controle de versão. | 24/10/2026 |

---

## 3. Detalhamento Técnico por Categoria de Fonte

### 3.1. Documentação Oficial do n8n e Guia de Workflows
- **Páginas:** [https://docs.n8n.io/](https://docs.n8n.io/) e [https://docs.n8n.io/workflows/](https://docs.n8n.io/workflows/)
- **Conhecimentos Extraídos e Aplicados:**
  - Todo workflow no n8n é representado internamente e exportado como um objeto JSON contendo pelo menos as chaves `name`, `nodes` (lista de objetos que definem id, nome, tipo, versão, posição `[x, y]` e parâmetros) e `connections` (mapa de adjacência ligando a saída `main` ou de sub-nós à entrada do próximo nó).
  - O fluxo de dados opera sobre listas de itens (`[ { "json": { ... } } ]`), onde cada nó processa os itens recebidos da etapa anterior.
- **Onde foi aplicado no projeto:** Na modelagem dos arquivos [`workflows/01-cadastro-de-leads/workflow.json`](../workflows/01-cadastro-de-leads/workflow.json), [`workflows/02-triagem-inteligente-ia/workflow.json`](../workflows/02-triagem-inteligente-ia/workflow.json) e nas regras do validador [`tests/validar-workflows.py`](../tests/validar-workflows.py).

### 3.2. Documentação de Webhooks e Respostas Síncronas
- **Páginas:** [Webhook Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) e [Respond to Webhook Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/)
- **Conhecimentos Extraídos e Aplicados:**
  - Para que um workflow receba dados via HTTP POST e devolva um resultado processado ao cliente na mesma chamada (como confirmar o cadastro de um lead ou informar erro de validação HTTP 400), o nó **Webhook** deve estar configurado com o parâmetro `responseMode: "responseNode"`, delegando o fechamento da requisição para um nó **Respond to Webhook** ao final de cada ramificação.
  - Os dados enviados no corpo da requisição HTTP POST ficam acessíveis tipicamente dentro de `$json.body` (ou diretamente em `$json` dependendo de como o payload é injetado em testes). Por isso, os workflows foram desenhados com normalização defensiva que aceita tanto `$json.body.campo` quanto `$json.campo`.
- **Onde foi aplicado no projeto:** Ambos os workflows utilizam a dupla `Webhook` + `Respond to Webhook` para fornecer respostas imediatas de sucesso e de erro sem depender de serviços externos.

### 3.3. Documentação de Nós de Controle e Transformação (`IF` e `Edit Fields / Set`)
- **Páginas:** [If Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) e [Edit Fields (Set) Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/)
- **Conhecimentos Extraídos e Aplicados:**
  - O nó **IF** (`n8n-nodes-base.if`) divide o fluxo em duas saídas (`main[0]` para **Verdadeiro / True** e `main[1]` para **Falso / False**). Isso permite isolar payloads incompletos ou fora do padrão logo no início do fluxo (*Fail-Fast*).
  - O nó **Edit Fields (Set)** (`n8n-nodes-base.set`) permite criar, renomear e higienizar propriedades JSON usando expressões como `.trim().toLowerCase()`, garantindo que etapas posteriores recebam um contrato de dados limpo.
- **Onde foi aplicado no projeto:** Na etapa de validação e preparação do Workflow 01 e na etapa de normalização e validação do Workflow 02.

### 3.4. Documentação sobre Agentes de IA e Modelos de Linguagem (Advanced AI)
- **Páginas:** [Advanced AI](https://docs.n8n.io/advanced-ai/) e [AI Agent Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/)
- **Conhecimentos Extraídos e Aplicados:**
  - O n8n implementa recursos de IA por meio de **Cluster Nodes** baseados em LangChain. O nó raiz **AI Agent** (`@n8n/n8n-nodes-langchain.agent`) recebe os dados do fluxo principal (`main`) e conecta-se a um sub-nó de modelo de linguagem (como `OpenAI Chat Model`, `@n8n/n8n-nodes-langchain.lmChatOpenAi`) através da conexão especial `ai_languageModel`.
  - Como modelos de linguagem são probabilísticos e exigem credenciais externas (`openAiApi`), uma arquitetura robusta de produção precisa:
    1. Fornecer um prompt de sistema estrito exigindo saída em formato JSON controlado (`categoria`, `prioridade`, `resumo`, `justificativa`).
    2. Validar e higienizar a resposta gerada antes de retorná-la ao solicitante.
    3. Prever fallback determinístico caso o modelo retorne formato inesperado ou caso o ambiente de demonstração esteja operando sem chave de API ativa.
- **Onde foi aplicado no projeto:** Em [`workflows/02-triagem-inteligente-ia/workflow.json`](../workflows/02-triagem-inteligente-ia/workflow.json) e no capítulo [`docs/04-miniestudo-final.md`](./04-miniestudo-final.md).

### 3.5. Repositório Oficial do n8n e Documentação do GitHub
- **Páginas:** [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n) e [docs.github.com — Sobre Repositórios](https://docs.github.com/pt/repositories/creating-and-managing-repositories/about-repositories)
- **Conhecimentos Extraídos e Aplicados:**
  - Verificação da estrutura de pacotes dos nós nativos e boas práticas de versionamento de projetos em repositórios Git públicos (uso de `README.md` na raiz e nos subdiretórios, `.gitignore` protegendo credenciais, `.gitattributes` para padronização de quebras de linha e `LICENSE` explícita).

---

## 4. Referências Conceituais sobre Engenharia de Prompts

Na modelagem dos templates da pasta [`prompts/`](../prompts/README.md) e do capítulo [`docs/03-engenharia-de-prompts.md`](./03-engenharia-de-prompts.md), foram aplicados padrões consolidados de engenharia de prompts voltados para especificação de software:

- **Role Prompting (Atribuição de Papel):** Direciona o espaço latente do modelo para o vocabulário e o rigor técnico de um Engenheiro de Software Sênior e Arquiteto n8n.
- **Context & Constraint Framing (Delimitação de Contexto e Restrições):** Impede que o modelo assuma acesso a credenciais reais, invente parâmetros de nós ou utilize sintaxes depreciadas.
- **Step-by-Step Decomposition (Decomposição em Etapas):** Estrutura o raciocínio em Entrada $\rightarrow$ Validação $\rightarrow$ Transformação $\rightarrow$ Processamento/IA $\rightarrow$ Saída e Tratamento de Erros.
- **Structured Output Specification (Especificação de Formato de Saída):** Define exatamente quais seções, tabelas e estruturas JSON a resposta da IA deve conter.

---

## 5. Limitações da Pesquisa e Cuidados Recomendados

1. **Evolução Rápida de Versões (`typeVersion` dos Nós):** O n8n atualiza frequentemente a versão interna de seus nós (`typeVersion`). Ao importar um `workflow.json` em uma versão futura ou anterior do n8n, a interface pode exibir um aviso sugerindo atualizar o nó para a revisão mais recente.
2. **Diferença entre Documentação Estática e Comportamento de Modelos Externos:** Embora a documentação do nó `AI Agent` defina como enviar instruções ao LLM, a qualidade da classificação depende do modelo escolhido (ex.: `gpt-4o-mini`, `gpt-4o`, `gemini-2.5-flash`) e da temperatura configurada. Por isso, o Workflow 02 inclui uma camada explícita de validação pós-IA.
3. **Recorte de Consulta:** A curadoria concentrou-se nos nós nativos essenciais para atender aos dois cenários do desafio com portabilidade máxima, evitando depender de *Community Nodes* de terceiros que exigiriam instalação adicional em instâncias *self-hosted*.
