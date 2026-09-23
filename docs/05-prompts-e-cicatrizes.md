# Engenharia de Prompts e Cicatrizes: Automação com n8n

---

## 📌 Visão Geral

Este documento registra a metodologia de **Engenharia de Prompts** aplicada ao estudo de Automação com n8n. Ele reúne **cinco experimentos práticos** desenhados para testar diferentes aspectos da ferramenta — desde conceitos estruturais e sintaxe de expressões até resiliência, segurança e agentes de inteligência artificial.

Cada experimento contrasta um **prompt original** com uma **versão aprimorada**, documentando as técnicas de prompting aplicadas, as limitações identificadas e as fontes oficiais obrigatórias para auditoria das respostas da IA. 

> **Nota:** Os campos de *Resposta Real Obtida* e *Registro de Cicatrizes e Alucinações* foram estruturados para que você possa inserir os resultados empíricos reais colhidos durante as suas sessões de testes com LLMs.

---

## 🧪 Experimento 1: Arquitetura e Fluxo de Dados (Item-Lists vs Iteração Tradicional)

### 1. Objetivo
Compreender como o n8n processa dados internamente através da estrutura de *item-lists* (listas de objetos JSON) e como isso se diferencia de loops e iteradores convencionais em linguagens de programação e outras ferramentas de automação.

### 2. Prompt Original
`	ext
Como funciona o fluxo de dados e os loops no n8n?
`

### 3. Resultado Esperado
Uma explicação clara e conceitual de que o n8n opera naturalmente em lote sobre arrays de itens ([ { json: { ... } } ]), executando a maioria dos nós uma vez para cada item sem a necessidade de um loop explícito, exceto em casos específicos de paginação ou controle com *Loop on Items*.

### 4. Limitações do Prompt Original
- **Ambiguidade**: É muito genérico e permite que a IA responda com conceitos genéricos de programação ou compare com Zapier/Make sem precisão técnica.
- **Risco de Alucinação**: Pode induzir a IA a sugerir que um loop manual sempre é obrigatório para processar múltiplos registros recebidos de um webhook ou banco.
- **Falta de Restrições**: Não delimita a versão do n8n nem exige exemplos de estruturas JSON reais.

### 5. Versão Melhorada
`	ext
[PERSONA]: Você é um Arquiteto de Software especialista em engenharia de integração e na plataforma n8n.
[CONTEXTO]: Estou estudando o modelo de execução interno do n8n para desenhar automações eficientes que processam listas de dados.
[TAREFA]: 
1. Explique detalhadamente como o n8n trata a estrutura de dados em item-lists (pares json e binary).
2. Explique a diferença entre a execução implícita (onde nós convencionais processam todos os itens recebidos) e a iteração explícita usando o nó Loop on Items (antigo Split In Batches).
3. Forneça um exemplo da estrutura JSON canônica de entrada e saída esperada por um nó n8n.
[RESTRIÇÕES]: 
- Baseie-se estritamente na versão estável moderna do n8n (v1.x+).
- Não invente nós inexistentes.
- Indique claramente quando um nó de loop é estritamente necessário (ex: controle de rate limit de APIs externas).
[FORMATO DE SAÍDA]: Explicação técnica estruturada em tópicos com blocos de código JSON demonstrativos.
`

### 6. Por que a Nova Versão é Melhor?
A nova versão aplica a técnica de **definição de persona**, contextualiza o objetivo, divide o problema em subtarefas bem delimitadas, estabelece restrições de versão (v1.x+) e exige o formato exato da estrutura canônica de dados do n8n, impedindo abstrações superficiais ou desatualizadas.

### 7. Fontes para Validação da Resposta
- **Fonte Oficial**: Documentação de Workflows e Fluxo de Dados do n8n ([https://docs.n8n.io/workflows/](https://docs.n8n.io/workflows/)).
- **Seção Específica**: Seções *Data structure in n8n* e *Looping in workflows*.

### 8. Registro de Teste Prático *(Para preenchimento posterior)*
- **Data do Teste**: [AAAA-MM-DD]
- **Modelo Utilizado**: [Ex: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro]
- **Resposta Real Obtida**:
  `	ext
  [Cole aqui a resposta gerada pelo modelo]
  `
- **Cicatrizes e Alucinações Observadas**:
  - *Houve menção a nós depreciados ou comportamento incorreto de listas? Registre aqui.*

---

## 🧪 Experimento 2: Sintaxe Moderna de Expressions e Prevenção de Métodos Descontinuados

### 1. Objetivo
Garantir a geração correta de expressões dinâmicas (expressions) no n8n moderno, evitando que a IA utilize sintaxes legadas descontinuadas na versão 1.0 (como o objeto antigo $node[Nome]).

### 2. Prompt Original
`	ext
Como faço para pegar o dado de um nó anterior no n8n usando código ou expressão?
`

### 3. Resultado Esperado
Demonstração das expressões $('Nome do Nó').item.json.campo e $('Nome do Nó').first().json.campo, explicando quando usar cada uma dependendo se o objetivo é referenciar o item pareado ou um valor global/primeiro item.

### 4. Limitações do Prompt Original
- **Alto Risco de Código Depreciado**: Como a base de treinamento dos LLMs possui muito conteúdo anterior à versão 1.0, o prompt genérico quase invariavelmente resulta na sintaxe desatualizada $node[Nome do Nó].json[campo].
- **Falta de Especificação de Cenário**: Não define se a referência é no editor visual de Expressions ou dentro de um *Code Node* (JavaScript/Python).

### 5. Versão Melhorada
`	ext
[PERSONA]: Você é um Engenheiro de Dados e Desenvolvedor n8n sênior.
[CONTEXTO]: Estou migrando e desenvolvendo workflows modernos no n8n (versão 1.x ou superior).
[TAREFA]: 
1. Demonstre a sintaxe correta e moderna recomendada pela documentação oficial para referenciar dados de nós anteriores em dois contextos:
   a) Dentro do editor de Expressões nativo (GUI).
   b) Dentro do nó Code Node (utilizando JavaScript).
2. Explique a diferença semântica e prática entre os métodos:
   - $('Nome').item.json.propriedade
   - $('Nome').first().json.propriedade
   - $('Nome').all()
3. Aponte explicitamente quais sintaxes antigas foram DESCONTINUADAS / NÃO RECOMENDADAS e por que seu uso deve ser evitado.
[RESTRIÇÕES]: 
- Não utilize $node[...] ou sintaxes de versões 0.x.
- Alerte sobre o impacto no pareamento de itens (item pairing).
`

### 6. Por que a Nova Versão é Melhor?
Bloqueia ativamente a armadilha mais frequente de LLMs no ecossistema n8n (o uso de sintaxes legadas), força a diferenciação entre expressões GUI e o *Code Node*, e exige a justificativa técnica sobre pareamento de itens (*item pairing*), que é crucial para evitar bugs silenciosos em produção.

### 7. Fontes para Validação da Resposta
- **Fonte Oficial**: Documentação de Expressões e Variáveis do n8n ([https://docs.n8n.io/workflows/expressions/](https://docs.n8n.io/workflows/expressions/)).
- **Seção Específica**: Seções *Expressions syntax* e *Referencing other nodes*.

### 8. Registro de Teste Prático *(Para preenchimento posterior)*
- **Data do Teste**: [AAAA-MM-DD]
- **Modelo Utilizado**: [Ex: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro]
- **Resposta Real Obtida**:
  `	ext
  [Cole aqui a resposta gerada pelo modelo]
  `
- **Cicatrizes e Alucinações Observadas**:
  - *O modelo tentou usar a sintaxe legada $node[...]? Responda aqui com a análise crítica.*

---

## 🧪 Experimento 3: Resiliência, Gestão de Falhas e Sub-workflows de Erro

### 1. Objetivo
Estruturar uma estratégia robusta de tratamento de exceções, alertas e reprocessamento automático de falhas em automações críticas no n8n.

### 2. Prompt Original
`	ext
Como tratar erros e reexecutar workflows com erro no n8n?
`

### 3. Resultado Esperado
Apresentação das duas principais camadas de tratamento de falhas do n8n: o tratamento em nível de nó (*Continue On Fail* / *Retry On Fail*) e o tratamento em nível de workflow (*Error Trigger Workflow* e histórico de execuções).

### 4. Limitações do Prompt Original
- Não especifica a severidade do fluxo ou o destino dos alertas.
- Deixa em aberto se o tratamento deve ser síncrono (no próprio fluxo) ou assíncrono (via workflow dedicado de tratamento de erros).
- Não aborda o ciclo de vida das execuções salvas no banco de dados.

### 5. Versão Melhorada
`	ext
[PERSONA]: Você é um Engenheiro de Confiabilidade (SRE) especializado em esteiras de automação corporativa.
[CONTEXTO]: Estou projetando uma arquitetura de alta resiliência para fluxos de integração críticos no n8n, onde falhas em APIs terceiras não podem causar perda silenciosa de dados.
[TAREFA]: 
1. Apresente as duas abordagens recomendadas pela documentação oficial para tratamento de erros:
   a) Configurações locais no nó (Retry On Fail, Continue On Fail).
   b) Configuração global de workflow de erro via nó Error Trigger.
2. Desenhe o passo a passo de como estruturar um workflow dedicado de tratamento de erro que capture o payload da falha (execution.id, workflow.name, mensagem de erro) e envie um alerta detalhado.
3. Explique como funciona o recurso operacional de reexecução (Retry failed execution) a partir do histórico de execuções do n8n.
[RESTRIÇÕES]: 
- Explique claramente as limitações de usar Continue On Fail sem sanitização posterior dos dados.
`

### 6. Por que a Nova Versão é Melhor?
A abordagem orientada a SRE define requisitos corporativos claros. Ela força a IA a cobrir a anatomia completa do nó *Error Trigger*, a explicar como o n8n passa metadados de execução para o fluxo de erro e a avaliar os riscos operacionais de mascarar erros ao usar *Continue On Fail*.

### 7. Fontes para Validação da Resposta
- **Fonte Oficial**: Documentação de Execuções e Tratamento de Erros ([https://docs.n8n.io/workflows/executions/](https://docs.n8n.io/workflows/executions/)).
- **Seção Específica**: Seção *Error workflows* e *Execution troubleshooting*.

### 8. Registro de Teste Prático *(Para preenchimento posterior)*
- **Data do Teste**: [AAAA-MM-DD]
- **Modelo Utilizado**: [Ex: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro]
- **Resposta Real Obtida**:
  `	ext
  [Cole aqui a resposta gerada pelo modelo]
  `
- **Cicatrizes e Alucinações Observadas**:
  - *A IA descreveu corretamente o payload injetado pelo nó Error Trigger?*

---

## 🧪 Experimento 4: Auditoria de Segurança e Hardening de Instâncias Self-Hosted

### 1. Objetivo
Identificar e aplicar as diretrizes oficiais de segurança, criptografia e isolamento para implantação do n8n em ambientes próprios (Self-Hosted via Docker/Docker Compose).

### 2. Prompt Original
`	ext
Quais são as dicas de segurança para instalar o n8n no meu servidor?
`

### 3. Resultado Esperado
Diretrizes formais de segurança: geração da chave simétrica de criptografia de credenciais, configuração de Task Runners para isolar o *Code Node*, restrição de acesso ao filesystem e execução do comando oficial 
8n audit.

### 4. Limitações do Prompt Original
- Produz conselhos genéricos de administração Linux (ex: use firewall e atualize o sistema) em vez de focar nas vulnerabilidades e vetores de ataque específicos da aplicação n8n.
- Ignora a ferramenta oficial de auditoria CLI do n8n.

### 5. Versão Melhorada
`	ext
[PERSONA]: Você é um Especialista em Segurança Ofensiva e DevSecOps especializado em aplicações baseadas em Node.js e orquestradores de workflow.
[CONTEXTO]: Estou realizando o deploy de uma instância corporativa do n8n self-hosted utilizando Docker Compose e preciso aplicar as recomendações oficiais de segurança e conformidade.
[TAREFA]: 
1. Explique a finalidade da variável de ambiente N8N_ENCRYPTION_KEY e o impacto crítico de sua perda ou vazamento.
2. Explique como funciona o comando nativo de auditoria de segurança da CLI do n8n (
8n audit), detalhando quais categorias de vulnerabilidade ele verifica.
3. Descreva as melhores práticas para mitigar riscos de Remote Code Execution (RCE) em nós de código personalizados (Code Node), incluindo o isolamento de Task Runners (N8N_RUNNERS_ENABLED).
4. Recomende a estratégia correta de autenticação e proteção para nós do tipo Webhook expostos à internet.
[RESTRIÇÕES]: 
- Baseie-se estritamente na seção oficial Security Audit da documentação do n8n.
`

### 6. Por que a Nova Versão é Melhor?
Direciona a IA para aspectos intrínsecos da arquitetura do n8n: segurança criptográfica das credenciais salvas, isolamento de processos para nós de código (mitigação de RCE) e comandos de auditoria nativos (
8n audit), transformando a resposta em um checklist acionável de DevSecOps.

### 7. Fontes para Validação da Resposta
- **Fonte Oficial**: Documentação de Auditoria de Segurança e Instalação ([https://docs.n8n.io/hosting/security-audit/](https://docs.n8n.io/hosting/security-audit/)).
- **Seção Específica**: Seções *Security audit CLI* e *Execution modes / Task runners*.

### 8. Registro de Teste Prático *(Para preenchimento posterior)*
- **Data do Teste**: [AAAA-MM-DD]
- **Modelo Utilizado**: [Ex: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro]
- **Resposta Real Obtida**:
  `	ext
  [Cole aqui a resposta gerada pelo modelo]
  `
- **Cicatrizes e Alucinações Observadas**:
  - *O modelo mencionou flags ou variáveis inexistentes? O comando de auditoria foi citado com precisão?*

---

## 🧪 Experimento 5: Integração de Inteligência Artificial e Agentes Autônomos (AI Nodes)

### 1. Objetivo
Arquitetar uma automação baseada nos nós modernos de IA do n8n (baseados no framework LangChain integrado), conectando um modelo de chat a ferramentas (*Tools*) e memória.

### 2. Prompt Original
`	ext
Como colocar IA no n8n para responder mensagens automaticamente?
`

### 3. Resultado Esperado
Explicação da arquitetura de nós de IA do n8n: o nó central *AI Agent* conectado a um nó de Modelo de Linguagem (ex: OpenAI Chat Model), um nó de Memória (ex: Window Buffer Memory) e nós de Ferramentas (*Tools* ou nós n8n convertidos em ferramentas).

### 4. Limitações do Prompt Original
- Quase certamente induzirá a IA a sugerir o nó básico e isolado da OpenAI (OpenAI Node), sem explicar o ecossistema avançado de agentes, recuperação de dados (RAG) ou ferramentas.
- Não diferencia chamadas de API simples de agentes autônomos orientados a tomada de decisão.

### 5. Versão Melhorada
`	ext
[PERSONA]: Você é um Arquiteto de Soluções de IA Generativa especializado no ecossistema n8n Advanced AI.
[CONTEXTO]: Preciso construir um fluxo inteligente no n8n que receba requisições de clientes via Webhook, consulte uma base de conhecimento e tome ações automatizadas.
[TAREFA]: 
1. Apresente a arquitetura dos nós modernos de IA do n8n (Advanced AI / LangChain integration).
2. Explique os papéis e a forma de conexão dos seguintes componentes fundamentais no canvas:
   - Nó raiz: AI Agent
   - Sub-nó: Chat Model (ex: OpenAI / Anthropic)
   - Sub-nó: Memory (ex: Window Buffer Memory / Postgres Chat Memory)
   - Sub-nó: Tools (ex: n8n Workflow as Tool / Calculator / HTTP Request)
3. Forneça o fluxo lógico e os cuidados técnicos para evitar que o agente entre em loops infinitos de execução de ferramentas.
[RESTRIÇÕES]: 
- Não limite a explicação ao nó simples legado de chamada direta da API da OpenAI.
- Foque na modelagem do nó AI Agent moderno.
`

### 6. Por que a Nova Versão é Melhor?
A versão aprimorada explora o estado da arte do n8n moderno, diferenciando claramente a integração ingênua com LLM da arquitetura modular de agentes cognitivos baseada em LangChain nativo, fornecendo uma base sólida para workflows de IA de nível profissional.

### 7. Fontes para Validação da Resposta
- **Fonte Oficial**: Documentação de AI do n8n ([https://docs.n8n.io/advanced-ai/](https://docs.n8n.io/advanced-ai/)).
- **Seção Específica**: Seções *AI Agent*, *Tools* e *Memory*.

### 8. Registro de Teste Prático *(Para preenchimento posterior)*
- **Data do Teste**: [AAAA-MM-DD]
- **Modelo Utilizado**: [Ex: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro]
- **Resposta Real Obtida**:
  `	ext
  [Cole aqui a resposta gerada pelo modelo]
  `
- **Cicatrizes e Alucinações Observadas**:
  - *O modelo explicou corretamente a conexão dos sub-nós (conectores inferiores do AI Agent)?*

---

## 📊 Matriz Comparativa dos Experimentos de Prompts

| Experimento | Domínio Técnico | Principal Risco de Alucinação / Falha | Técnica de Melhoria Aplicada | Fonte de Validação |
| :--- | :--- | :--- | :--- | :--- |
| **Exp. 1** | Fluxo de Dados e Listas | Confundir listas de itens com loops tradicionais obrigatórios | Persona + Restrições de versão (v1.x) + JSON Canônico | docs.n8n.io/workflows/ |
| **Exp. 2** | Sintaxe de Expressões | Uso de sintaxe legada descontinuada ($node[...]) | Bloqueio explícito de termos obsoletos + Diferenciação GUI vs Code Node | docs.n8n.io/workflows/expressions/ |
| **Exp. 3** | Resiliência e Falhas | Mascarar erros com *Continue on Fail* sem alerta | Engenharia SRE + Estrutura formal do nó *Error Trigger* | docs.n8n.io/workflows/executions/ |
| **Exp. 4** | Segurança e Hardening | Recomendações genéricas de SO ignorando o aplicativo | Foco em DevSecOps + Comando nativo 
8n audit + Task Runners | docs.n8n.io/hosting/security-audit/ |
| **Exp. 5** | Agentes de IA | Foco no nó simples da OpenAI em vez da arquitetura de agentes | Decomposição de sub-nós (Model, Memory, Tools) + Prevenção de loop | docs.n8n.io/advanced-ai/ |
