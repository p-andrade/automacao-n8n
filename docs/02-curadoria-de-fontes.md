# 2. Curadoria de Fontes: Automação com n8n

---

## 🔍 Metodologia de Seleção e Validação

Para a construção deste miniestudo e de seu acervo de automações, adotou-se um protocolo rigoroso de curadoria com foco em **fontes técnicas primárias e documentação oficial mantida pelos criadores do n8n**. 

### Critérios de Curadoria:
- **Autoridade e Autoria**: Priorização da documentação mantida diretamente pela equipe de engenharia do n8n.
- **Acurácia Técnica e Atualidade**: Eliminação de métodos legados (ex: sintaxes antigas de JavaScript, nós descontinuados e parâmetros obsoletos de APIs).
- **Auditabilidade e Segurança**: Consulta a diretrizes oficiais sobre gestão segura de credenciais, execução de código isolado e mitigação de vulnerabilidades.

---

## 📚 Catálogo Estruturado de Fontes Oficiais

---

### Fonte 1 — Documentação Geral e Visão de Plataforma
- **Título**: n8n Documentation: Overview, Setup and Integrations
- **Organização/Autoria**: n8n GmbH
- **URL**: [https://docs.n8n.io/](https://docs.n8n.io/)
- **Tipo de Fonte**: Documentação técnica oficial (Portal raiz)
- **Principais Conceitos Abordados**:
  - Arquitetura de plataforma iPaaS e modelo de execução de fluxos de nós.
  - Modos de instalação e deploy (n8n Cloud, Docker container, Kubernetes, npm).
  - Catálogo de centenas de nós de integração (Core Nodes e Community Nodes).
  - Capacidades integradas de IA (Advanced AI / LangChain).
- **Por que a fonte foi selecionada**: Trata-se da autoridade máxima sobre a ferramenta, servindo como o alicerce oficial para especificações técnicas, parâmetros e guias de instalação.
- **Quais partes do miniestudo ela ajudará a fundamentar**:
  - Seção 1 (Introdução ao n8n e Proposta de Valor).
  - Seção 3 (Modelo de Deploy: Cloud vs. Self-Hosted).
- **Limitações da Fonte**: Por ser a documentação geral de alto nível, alguns cenários complexos de infraestrutura distribuída em larga escala exigem consulta complementar à documentação de orquestração (Docker/Kubernetes).

---

### Fonte 2 — Conceitos Centrais, Lógica de Workflows e Dados
- **Título**: Core Workflow Concepts and Data Flow in n8n
- **Organização/Autoria**: n8n GmbH
- **URL**: [https://docs.n8n.io/workflows/](https://docs.n8n.io/workflows/)
- **Tipo de Fonte**: Documentação técnica oficial (Guia de Arquitetura e Lógica)
- **Principais Conceitos Abordados**:
  - Ciclo de vida dos dados e estrutura de objetos em pares JSON / Binary.
  - Controle de fluxo e nós lógicos (*If*, *Switch*, *Loop on Items / Split In Batches*, *Merge*, *Wait*).
  - Sub-workflows modulares via nós *Execute Workflow Trigger* e *Execute Workflow*.
  - Expressões dinâmicas n8n e sintaxe moderna de referências ($('Node Name').item.json.campo).
  - Manipulação de código e lógica personalizada com o *Code Node* (JavaScript e Python).
- **Por que a fonte foi selecionada**: Essencial para fundamentar a lógica correta de fluxo de dados no n8n, garantindo que o estudo não confunda o modelo baseado em listas de itens (*item-lists*) com iteradores lineares convencionais.
- **Quais partes do miniestudo ela ajudará a fundamentar**:
  - Seção 2 (Componentes Fundamentais e Fluxo de Dados).
  - [05-glossario.md](05-glossario.md) (Definição precisa de nós e operadores).
  - [prompts/prompt-design-workflow.md](../prompts/prompt-design-workflow.md).
- **Limitações da Fonte**: As expressões com sintaxe n8n mudaram significativamente em relação a versões anteriores à 1.0 (sintaxe $node[...]), o que exige atenção redobrada do leitor para não misturar referências legadas encontradas em tutoriais de terceiros.

---

### Fonte 3 — Gestão, Monitoramento e Resiliência de Execuções
- **Título**: Execution Lifecycle, Troubleshooting and Retries
- **Organização/Autoria**: n8n GmbH
- **URL**: [https://docs.n8n.io/workflows/executions/](https://docs.n8n.io/workflows/executions/)
- **Tipo de Fonte**: Manual operacional oficial
- **Principais Conceitos Abordados**:
  - Ciclo de estados de execução: *Running*, *Success*, *Waiting*, *Error*, *Crashed*.
  - Inspeção e depuração de payloads de entrada/saída nó a nó no painel de execuções.
  - Mecanismos de tolerância a falhas: *Error Trigger node*, fluxos de fallback e reexecução de falhas (*Retry Failed Executions*).
  - Pruning e retenção de logs de execução para controle de armazenamento no banco de dados.
- **Por que a fonte foi selecionada**: Automações em produção dependem de resiliência e observabilidade; esta fonte estabelece os padrões da plataforma para auditoria de falhas e reprocessamento.
- **Quais partes do miniestudo ela ajudará a fundamentar**:
  - Seção 5 (Boas Práticas e Tratamento de Erros).
  - [prompts/prompt-troubleshooting.md](../prompts/prompt-troubleshooting.md).
- **Limitações da Fonte**: O armazenamento massivo de dados binários em execuções detalhadas pode degradar instâncias menores com SQLite; o guia aborda a operação do software, mas não cobre aprofundadamente o dimensionamento de bases de dados externas como PostgreSQL em alta concorrência.

---

### Fonte 4 — Segurança, Auditoria e Hardening de Instâncias
- **Título**: Security Audit and Instance Hardening
- **Organização/Autoria**: n8n GmbH
- **URL**: [https://docs.n8n.io/hosting/security-audit/](https://docs.n8n.io/hosting/security-audit/)
- **Tipo de Fonte**: Guia de segurança e conformidade oficial
- **Principais Conceitos Abordados**:
  - Comando nativo de auditoria de segurança da instância (
8n audit).
  - Criptografia simétrica de credenciais armazenadas (N8N_ENCRYPTION_KEY).
  - Isolamento de execução de código no *Code Node* (Task Runners e sandboxing).
  - Controle de privilégios de sistema de arquivos e variáveis de ambiente sensíveis.
  - Boas práticas para endpoints de Webhooks públicos e autenticação (Header Auth, Basic Auth, OAuth2).
- **Por que a fonte foi selecionada**: A automação corporativa lida frequentemente com segredos, tokens e dados sensíveis; comprova a viabilidade técnica e conformidade de segurança do n8n em ambientes profissionais.
- **Quais partes do miniestudo ela ajudará a fundamentar**:
  - Seção 3 (Modelo de Deploy: Cloud vs. Self-Hosted).
  - Seção 5 (Boas Práticas e Segurança de Credenciais).
- **Limitações da Fonte**: A ferramenta de auditoria automática foca nas configurações internas da instância n8n; políticas de segurança perimetral (como Web Application Firewalls, Cloudflare Rules e VPNs de borda) ficam a cargo da infraestrutura do cliente e não são escopo do documento.

---

### Fonte 5 — Repositório Oficial de Modelos e Casos Práticos
- **Título**: n8n Workflow Templates Library
- **Organização/Autoria**: n8n Community & n8n GmbH
- **URL**: [https://n8n.io/workflows/](https://n8n.io/workflows/)
- **Tipo de Fonte**: Catálogo prático e repositório de templates oficiais
- **Principais Conceitos Abordados**:
  - Padrões arquiteturais consolidados para integração de serviços (Slack, OpenAI, Google Sheets, bancos de dados, CRMs).
  - Estruturação de payloads em formato JSON para importação direta via copiar/colar.
  - Implementação de nós de IA conectados a modelos de linguagem (Chat Models, Memory, Tools, Vector Stores).
- **Por que a fonte foi selecionada**: Fornece os benchmarks da indústria para composição de fluxos, garantindo que os exemplos do portfólio sigam convenções reais de mercado.
- **Quais partes do miniestudo ela ajudará a fundamentar**:
  - Seção 4 (Integração com Inteligência Artificial).
  - Os diretórios práticos workflows/01-webhook-to-slack-notif/ e workflows/02-ia-agent-triage/.
- **Limitações da Fonte**: Como o repositório é alimentado tanto pela equipe n8n quanto pela comunidade, alguns templates antigos podem conter nós desatualizados ou exigir credenciais de serviços pagos de terceiros para teste completo.

---

## ⚠️ Avaliação Crítica Geral e Cuidados Técnicos

1. **Prevenção de Alucinações de Sintaxe**: Versões modernas do n8n substituíram o acesso legado a variáveis. O estudo adota exclusivamente a sintaxe recomendada pela documentação oficial ($('Nome do Nó').item.json...).
2. **Separação de Contexto (Cloud vs. Self-Hosted)**: Determinadas diretivas de infraestrutura (como volumes de filesystem e Task Runners de isolamento de código) aplicam-se estritamente a instâncias *Self-hosted*, sendo gerenciadas de forma transparente na modalidade *n8n Cloud*.
