# 4. Glossário Técnico de Conceitos: n8n e Automação

---

## 📌 Visão Geral

Este glossário reúne os principais termos, componentes e padrões arquiteturais fundamentais para o desenvolvimento, governança e operação de automações na plataforma n8n, alinhado à documentação técnica oficial da ferramenta.

---

## 📖 Dicionário de Termos Técnicos

### 1. Workflow
- **Definição Técnica**: Grafo acíclico direcionado (DAG) composto por nós e conexões que define a lógica sequencial ou paralela de uma esteira de automação.
- **Contexto no n8n**: É a unidade principal de desenvolvimento e execução na plataforma, armazenável em formato estruturado JSON para controle de versão e portabilidade.

### 2. Trigger (Nó Gatilho)
- **Definição Técnica**: Evento ou listener responsável por iniciar o ciclo de vida de uma execução em um workflow.
- **Contexto no n8n**: Nó inicial (sem entrada à esquerda). Pode ser baseado em eventos externos (ex: Webhook, Telegram Trigger), em agendamento temporal (ex: Schedule Trigger) ou acionado programaticamente por outro fluxo (Execute Workflow Trigger).

### 3. Node (Nó)
- **Definição Técnica**: Bloco modular de processamento ou integração que executa uma função atômica e específica dentro da esteira.
- **Contexto no n8n**: Divide-se entre *Core Nodes* (nós de controle lógico, transformação de dados e requisições HTTP) e *Integration Nodes* (conectores oficiais para serviços de terceiros como Slack, Google, AWS, OpenAI).

### 4. Webhook
- **Definição Técnica**: Padrão de comunicação assíncrona orientada a eventos (*HTTP callbacks*), onde um sistema envia uma requisição HTTP com payload JSON para uma URL externa assim que um evento ocorre.
- **Contexto no n8n**: O nó Webhook expõe endpoints HTTP (de teste e de produção) para receber dados de formulários, sistemas de pagamento, plataformas de CRM e eventos do GitHub.

### 5. API (Application Programming Interface)
- **Definição Técnica**: Conjunto de protocolos, rotinas e definições padronizadas que permitem a comunicação e troca de dados entre diferentes aplicações de software.
- **Contexto no n8n**: O nó HTTP Request permite consumir qualquer API REST/GraphQL pública ou privada, fornecendo suporte nativo a múltiplos padrões de autenticação (OAuth2, Bearer Token, API Key, Basic Auth).

### 6. Expression (Expressão Dinâmica)
- **Definição Técnica**: Mecanismo de interpolação e avaliação de código em tempo de execução para mapear valores dinâmicos de nós anteriores em parâmetros de nós subsequentes.
- **Contexto no n8n**: Expressões são delimitadas por chaves duplas {{ ... }} e utilizam JavaScript puro e objetos nativos como $('Nome do Nó').item.json.campo.

### 7. Execution (Execução)
- **Definição Técnica**: Instância individualizada de processamento de um workflow acionado por um gatilho.
- **Contexto no n8n**: Cada execução recebe um identificador único (execution.id) e registra o histórico completo de entrada/saída de cada nó, duração e estado operacional (*Success*, *Error*, *Running*, *Waiting*).

### 8. Credential (Credencial)
- **Definição Técnica**: Conjunto seguro de parâmetros de autenticação (tokens, chaves secretas, certificados ou credenciais OAuth) necessários para autorizar requisições a serviços externos.
- **Contexto no n8n**: Armazenadas de forma centralizada e desacoplada dos workflows. No banco de dados da instância, são protegidas por criptografia simétrica com a chave N8N_ENCRYPTION_KEY.

### 9. Automation (Automação de Processos)
- **Definição Técnica**: Aplicação de regras lógicas e tecnologia para executar tarefas recorrentes sem ou com mínima intervenção humana, reduzindo latência operacional e eliminando erros manuais.
- **Contexto no n8n**: Traduz regras de negócio em fluxos integrados que orquestram tráfego de dados entre bancos, ferramentas de comunicação e modelos de inteligência artificial.

### 10. Self-Hosted (Implantação Autogerenciada)
- **Definição Técnica**: Modelo de implantação em que a aplicação é instalada e operada diretamente na infraestrutura própria do usuário (servidores dedicados, VPS, Docker, Kubernetes).
- **Contexto no n8n**: Alternativa ao serviço gerenciado *n8n Cloud*. Garante soberania total de dados, ausência de limites arbitrários de execuções por plano comercial e conformidade com leis de privacidade de dados.

---

## 🛠️ Termos Avançados de Arquitetura n8n

| Termo Avançado | Definição e Aplicação Prática |
| :--- | :--- |
| **Item-List** | Estrutura de dados padrão do n8n onde informações trafegam como um array de objetos JSON, permitindo processamento em lote automático sem necessidade de loops forçados. |
| **Data Pinning** | Recurso do editor visual que permite fixar dados de teste em nós específicos, acelerando o desenvolvimento de expressões sem necessidade de reexecutar nós anteriores. |
| **Code Node** | Nó de computação avançada que permite executar código JavaScript moderno ou Python nativo diretamente dentro da esteira de dados. |
| **Sub-workflow** | Workflow modular invocado por outro fluxo através do nó *Execute Workflow*, promovendo o reuso de código e simplificação de esteiras complexas. |
| **Error Trigger** | Gatilho especializado que é disparado automaticamente pela plataforma sempre que um workflow associado falha criticamente, permitindo alarmes e contingências. |
