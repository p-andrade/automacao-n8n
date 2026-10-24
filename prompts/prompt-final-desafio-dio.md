# 🏆 Prompt Final — Desafio DIO: Planejando Automações com n8n Usando Apenas Bons Prompts

> **Navegação:** [🏠 README Principal](../README.md) | [📋 Catálogo de Prompts](./README.md) | [⚙️ Ver Workflow 01 Implementado](../workflows/01-cadastro-de-leads/README.md) | [📚 Documentação Técnica](../docs/README.md)

---

## 📌 Sobre Este Documento (Entrega Principal da DIO)

Este é o **artefato principal de entrega** para o desafio da **DIO (Digital Innovation One)**: *Planejando Automações com n8n Usando Apenas Bons Prompts*.

Ele foi construído de forma **100% autossuficiente**: mesmo que o leitor não consulte nenhum outro arquivo deste repositório, encontrará aqui todo o raciocínio estruturado nas **3 Etapas Oficiais do Desafio**, exemplificado com o cenário completo de **Cadastro Automatizado de Leads**, além do **Prompt Final Pronto para Copiar e Utilizar** em qualquer Modelo de Linguagem moderno (ChatGPT, Claude, Gemini, Copilot).

---

## 🧭 Etapa 1 — Definir a Automação Desejada

Antes de escrever o comando para a Inteligência Artificial, definimos com clareza qual tarefa repetitiva será automatizada, quem será beneficiado e qual resultado mensurável esperamos alcançar.

| Dimensão | Especificação Planejada |
| :--- | :--- |
| **1. Processo (Tarefa Repetitiva)** | **Recepção, Validação, Higienização e Preparação de Cadastro de Leads Comerciais.** Atualmente, quando um visitante preenche um formulário em uma página de captura (*landing page*), os dados chegam brutos (com espaços extras, e-mails em letras maiúsculas, campos opcionais vazios ou até e-mails inválidos). Fazer essa conferência, padronização e aviso à equipe comercial de forma manual consome tempo e gera perda de oportunidades. |
| **2. Público ou Responsável Beneficiado** | **Equipes Comerciais (SDRs / Vendedores), Analistas de Marketing e Operações (RevOps)**, além de estudantes e profissionais iniciantes em automação que precisam de um fluxo confiável para qualificar a entrada de contatos sem retrabalho manual. |
| **3. Resultado Esperado** | Um workflow automatizado no **n8n** que receba os dados do lead instantaneamente via HTTP `POST` (*Webhook*), valide se o nome e o e-mail são válidos, higienize e padronize os campos, monte uma estrutura pronta para registro/notificação comercial e devolva imediatamente ao sistema chamador uma resposta HTTP estruturada (`200 OK` para sucesso ou `400 Bad Request` para dados inválidos). |

---

## ⚙️ Etapa 2 — Adicionar Contexto e Regras

Com o objetivo definido, estabelecemos o ecossistema técnico, o desenho do fluxo, as regras de negócio estritas, as restrições de segurança e o comportamento diante de exceções.

### 2.1. Ferramentas Envolvidas
- **Plataforma de Orquestração:** **n8n** (compatível com versões modernas `v1.x` e `v2.x`, validado na estrutura `v2.42.7`), utilizando exclusivamente **nós nativos (*Core Nodes*)** para garantir portabilidade imediata sem exigir contas pagas ou credenciais externas para teste:
  1. `Webhook` (`n8n-nodes-base.webhook`) — Porta de entrada HTTP `POST`.
  2. `IF` (`n8n-nodes-base.if`) — Motor de decisão condicional (*Fail-Fast*).
  3. `Edit Fields (Set)` (`n8n-nodes-base.set`) — Higienização, normalização e montagem do payload.
  4. `Respond to Webhook` (`n8n-nodes-base.respondToWebhook`) — Retorno síncrono HTTP (`200` ou `400`).

### 2.2. Fluxo Desejado (Sequência Lógica)
1. **Recepção:** O nó `Webhook Receber Lead` recebe um payload JSON via requisição `POST /cadastro-leads`.
2. **Validação Condicional:** O nó `Validar Dados do Lead` (`IF`) verifica se os campos obrigatórios atendem às regras.
3. **Ramificação de Sucesso (`True`):**
   - O nó `Preparar Registro do Lead` (`Edit Fields / Set`) limpa espaços, converte o e-mail para minúsculas, preenche valores padrão para campos opcionais e adiciona carimbo de tempo e identificador do lead.
   - O nó `Montar Notificacao Demonstrativa` (`Edit Fields / Set`) formata o resumo executivo para a equipe comercial e define o status de processamento.
   - O nó `Responder Sucesso` (`Respond to Webhook`) retorna HTTP `200 OK` com o JSON completo processado.
4. **Ramificação de Erro (`False`):**
   - O nó `Responder Erro Validacao` (`Respond to Webhook`) interrompe o processamento inválido e retorna imediatamente HTTP `400 Bad Request` explicando o motivo da rejeição.

### 2.3. Regras de Negócio
- **RN01 (Obrigatoriedade do Nome):** O campo `nome` é obrigatório e, após remoção de espaços nas extremidades (`.trim()`), deve possuir pelo menos 2 caracteres.
- **RN02 (Obrigatoriedade e Formato de E-mail):** O campo `email` é obrigatório e deve conter obrigatoriamente o caractere `@` e pelo menos um ponto `.` após higienização.
- **RN03 (Normalização de Dados):**
  - `nome`: remover espaços excedentes nas pontas (`.trim()`).
  - `email`: remover espaços e converter integralmente para letras minúsculas (`.trim().toLowerCase()`).
  - `telefone`, `empresa`, `origem` e `interesse`: campos opcionais; se não forem enviados no payload, devem receber valores padrão explícitos (`"Não informado"` ou `" Orgânico / Direto"`), evitando valores `null` ou `undefined` na saída.
- **RN04 (Rastreabilidade):** Todo lead válido preparado deve receber um código de protocolo demonstrativo (`lead_id`) e a data/hora ISO 8601 do processamento (`processado_em`).

### 2.4. Restrições Técnicas e de Segurança
- **RT01 (Zero Credenciais Expostas):** O workflow e o prompt jamais devem incluir chaves de API, tokens, senhas ou dados reais de terceiros.
- **RT02 (Honestidade de Persistência):** Para permitir testes sem banco de dados externo configurado, a etapa de registro e notificação deve operar em **modo demonstrativo estruturado**, retornando os objetos prontos via `Respond to Webhook`, sem afirmar falsamente que o registro foi gravado em um banco externo não conectado.
- **RT03 (Sintaxe Moderna do n8n):** É proibido utilizar a sintaxe legada `$node["Nome"]` (depreciada desde o n8n 1.0). Deve-se usar apenas `$json` e `$('Nome do Nó').item.json`.

### 2.5. Tratamento de Exceções
- **Exceção 1 — Payload Vazio ou Campos Obrigatórios Ausentes (`nome` ou `email` faltando):** O nó `IF` desvia para o ramo `false` e retorna HTTP `400` com mensagem clara.
- **Exceção 2 — E-mail Malformado (ex.: `"usuario_sem_arroba.com"`):** O nó `IF` reprova na checagem de formato e desvia para o ramo `false` (HTTP `400`).
- **Exceção 3 — Diferença de Encapsulamento do Corpo HTTP (`$json.body` vs `$json`):** As expressões devem acessar os campos de forma resiliente (`$json.body?.campo ?? $json.campo`), funcionando tanto em chamadas HTTP externas quanto em execuções manuais de teste no editor do n8n.

---

## 🚀 Etapa 3 — Montar o Prompt Final (Pronto para Copiar e Utilizar)

Copie integralmente o bloco abaixo e cole no seu assistente de Inteligência Artificial para gerar a proposta arquitetural completa, documentada e acompanhada do JSON exportável para o n8n:

```markdown
# PROMPT PARA ARQUITETURA E GERAÇÃO DE WORKFLOW NO N8N — CADASTRO AUTOMATIZADO DE LEADS

## 1. PAPEL DA IA
Atue como um Engenheiro de Software Sênior, Arquiteto de Automações especialista em n8n (versões modernas v1.x e v2.x) e Designer Instrucional Técnico. Sua comunicação deve ser em português brasileiro, clara, precisa, didática para iniciantes e rigorosa tecnicamente.

## 2. CONTEXTO
Uma equipe comercial recebe cadastros de potenciais clientes (leads) vindos de formulários web e landing pages. Atualmente, muitos cadastros chegam com espaços desnecessários, e-mails em caixa alta, campos opcionais ausentes ou até mesmo sem nome ou com e-mail inválido, gerando retrabalho manual e atraso no atendimento.
Você não possui (e não deve presumir que possui) acesso direto às contas, bancos de dados, CRMs ou credenciais privadas do usuário. Portanto, sua missão é projetar uma solução autocontida, segura e pronta para ser importada e testada localmente no n8n.

## 3. OBJETIVO
Projetar, explicar detalhadamente e gerar o arquivo JSON de um workflow demonstrativo no n8n chamado **"01 - Cadastro Automatizado de Leads"**, que receba os dados de um lead via Webhook, valide os campos obrigatórios, normalize e prepare os dados para registro/notificação e retorne uma resposta HTTP estruturada tanto em caso de sucesso quanto em caso de erro de validação.

## 4. PÚBLICO-ALVO
Estudantes de tecnologia, iniciantes em automação de processos com n8n e desenvolvedores que desejam compreender visual e tecnicamente como cada nó transforma e valida os dados ao longo do fluxo.

## 5. FERRAMENTAS E NÓS N8N RECOMENDADOS
Utilize exclusivamente nós nativos (*Core Nodes*) do pacote `n8n-nodes-base`, mantendo exatamente os seguintes nomes em português para garantir consistência entre documentação, diagramas e JSON:
1. **`Webhook Receber Lead`** (`n8n-nodes-base.webhook`) — Gatilho HTTP `POST` no caminho `cadastro-leads`, configurado com `responseMode: "responseNode"`.
2. **`Validar Dados do Lead`** (`n8n-nodes-base.if`) — Nó condicional que verifica as regras de obrigatoriedade e formato.
3. **`Preparar Registro do Lead`** (`n8n-nodes-base.set` / Edit Fields) — Nó do caminho de sucesso (`true`) que limpa e padroniza os dados do lead.
4. **`Montar Notificacao Demonstrativa`** (`n8n-nodes-base.set` / Edit Fields) — Nó que estrutura o pacote final com o resumo da notificação comercial demonstrativa e metadados de processamento.
5. **`Responder Sucesso`** (`n8n-nodes-base.respondToWebhook`) — Nó que encerra o caminho feliz retornando HTTP `200 OK` com o JSON processado.
6. **`Responder Erro Validacao`** (`n8n-nodes-base.respondToWebhook`) — Nó conectado à saída `false` da validação que retorna imediatamente HTTP `400 Bad Request` quando o payload é inválido.

## 6. ETAPAS DO FLUXO E REGRAS DE NEGÓCIO
O workflow deve obedecer rigorosamente a esta lógica:
- **Etapa 1 (Entrada):** Receber um JSON contendo `nome`, `email`, `telefone`, `empresa`, `origem` e `interesse` (acessível via `$json.body` ou diretamente em `$json`).
- **Etapa 2 (Validação):** Verificar se `nome` (após `.trim()`) não está vazio E se `email` (após `.trim()`) contém `@` e `.`.
- **Etapa 3 (Preparação no Caminho True):**
  - `lead_id`: gerar identificador demonstrativo (ex.: `"LEAD-" + $execution.id` ou timestamp).
  - `nome`: string limpa com `.trim()`.
  - `email`: string limpa e em minúsculas com `.trim().toLowerCase()`.
  - `telefone`: valor limpo ou `"Não informado"` se ausente.
  - `empresa`: valor limpo ou `"Não informada"` se ausente.
  - `origem`: valor limpo ou `" Direto / Não especificada"` se ausente.
  - `interesse`: valor limpo ou `"Geral"` se ausente.
  - `processado_em`: data/hora atual em formato ISO 8601 (`$now.toISO()`).
- **Etapa 4 (Notificação Demonstrativa):** Criar um objeto `notificacao_comercial` contendo `canal_sugerido` (`"#comercial-leads"`), `assunto`, `mensagem_formatada` e `status_persistencia` (`"demonstrativo_pronto_para_integracao"`), deixando claro que nenhum serviço externo foi acionado sem credencial.
- **Etapa 5 (Saída):** Retornar o JSON estruturado via `Respond to Webhook`.

## 7. TRATAMENTO DE ERROS E RESTRIÇÕES OBRIGATÓRIAS
- **Caminho de Erro (HTTP 400):** Se `nome` estiver vazio ou `email` for inválido, o fluxo NÃO deve passar pelos nós de preparação; deve ir direto da saída `false` do nó `Validar Dados do Lead` para `Responder Erro Validacao`, retornando `status: "erro_validacao"`, `codigo_http: 400` e uma mensagem orientando a correção.
- **Sintaxe de Expressões:** Utilize EXCLUSIVAMENTE a sintaxe moderna do n8n (`$json`, `$('Nome do Nó').item.json`). NUNCA utilize a sintaxe depreciada `$node["..."]`.
- **Segurança:** NUNCA inclua credenciais, tokens, chaves de API ou segredos reais no JSON.
- **Integridade do Grafo:** Na seção `connections` do JSON, certifique-se de que as chaves de origem e as propriedades `node` de destino tenham grafia idêntica (incluindo maiúsculas/minúsculas e espaços) à propriedade `name` declarada na lista `nodes`.

## 8. CRITÉRIOS DE VALIDAÇÃO DA RESPOSTA
Antes de concluir sua resposta, verifique internamente:
1. Os 6 nós listados estão presentes no JSON com nomes únicos e coordenadas `[x, y]` organizadas?
2. O nó `Webhook Receber Lead` possui `responseMode: "responseNode"`?
3. O nó `Validar Dados do Lead` possui a saída `main[0]` conectada a `Preparar Registro do Lead` e a saída `main[1]` conectada a `Responder Erro Validacao`?
4. O JSON gerado é 100% válido sintaticamente (sem comentários `//` dentro do bloco JSON e sem vírgulas sobrando)?

## 9. FORMATO DE ENTREGA ESPERADO
Estruture sua resposta exatamente nesta ordem:
1. **Visão Geral da Solução:** Resumo executivo da automação proposta.
2. **Diagrama de Fluxo em Mermaid (`flowchart LR`):** Representando os 6 nós e os caminhos `True` (Sucesso) e `False` (Erro).
3. **Explicação Didática Nó a Nó:** Tabela ou seções explicando para cada um dos 6 nós: função, entrada, processamento, saída e comportamento de erro.
4. **Arquivo JSON do Workflow (`workflow.json`):** Bloco de código `json` completo e pronto para salvar e importar no n8n.
5. **Exemplos de Teste (Payloads e Respostas):**
   - Um exemplo de payload válido (`POST`) e o JSON esperado no retorno `HTTP 200`.
   - Um exemplo de payload inválido (`POST` sem e-mail válido) e o JSON esperado no retorno `HTTP 400`.
6. **Guia Rápido de Evolução para Produção:** Como o usuário pode conectar futuramente sua própria conta do Google Sheets, PostgreSQL, HubSpot ou Slack usando o sistema seguro de Credentials do n8n.
```

---

## 🔗 Onde Ver o Resultado Prático Deste Prompt no Repositório?

Para comprovar na prática o funcionamento do prompt acima, todo o resultado gerado e validado já está implementado neste projeto:

1. **Workflow JSON Implementado:** [`workflows/01-cadastro-de-leads/workflow.json`](../workflows/01-cadastro-de-leads/workflow.json)
2. **Documentação Ilustrada Nó a Nó:** [`workflows/01-cadastro-de-leads/README.md`](../workflows/01-cadastro-de-leads/README.md)
3. **Payload de Exemplo Pronto para Teste:** [`workflows/01-cadastro-de-leads/exemplo-payload.json`](../workflows/01-cadastro-de-leads/exemplo-payload.json)
4. **Diagrama Mermaid Correspondente:** [`assets/diagrams/fluxo-cadastro-leads.mmd`](../assets/diagrams/fluxo-cadastro-leads.mmd)
5. **Segundo Workflow Avançado (Triagem Inteligente com IA):** [`workflows/02-triagem-inteligente-ia/README.md`](../workflows/02-triagem-inteligente-ia/README.md)
