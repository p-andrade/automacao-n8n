# 03. Engenharia de Prompts Aplicada a Automações no n8n

> **Navegação:** [⬅️ 02. Curadoria de Fontes](./02-curadoria-de-fontes.md) | [📚 Índice da Documentação](./README.md) | [Próximo: 04. Miniestudo Final ➡️](./04-miniestudo-final.md)

---

## 1. Introdução: Por que Planejar Automações com Prompts?

Construir um workflow no **n8n** envolve traduzir regras de negócio do mundo real em um grafo direcionado de nós, expressões JavaScript e contratos JSON. Quando um profissional recorre a Modelos de Linguagem (LLMs) para planejar ou gerar uma automação sem fornecer estrutura técnica, o modelo preenche as lacunas com suposições genéricas — resultando em fluxos sem validação de entrada, sem tratamento de erros ou com código incompatível.

A **Engenharia de Prompts para Automação** resolve esse problema tratando o prompt como uma **especificação de arquitetura**. Neste capítulo, detalhamos os 12 pilares que compõem um prompt de nível profissional para o n8n, comparamos exemplos *Antes vs. Depois* e documentamos como diagnosticar e corrigir falhas comuns geradas por IA.

---

## 2. Os 12 Pilares de um Prompt Estruturado para n8n

Para que uma Inteligência Artificial projete um workflow confiável, o prompt deve contemplar 12 dimensões fundamentais:

### 2.1. Definição do Papel da IA (Persona)
Atribui ao modelo a especialidade, o nível de senioridade e o foco técnico esperados.
- **Como aplicar:** *"Atue como um Engenheiro de Software Sênior e Arquiteto de Automações especialista em n8n (v1.x/v2.x), integrações REST/Webhook e governança de dados."*

### 2.2. Contexto
Explica o cenário organizacional, o problema atual e o motivo pelo qual a automação está sendo criada.
- **Como aplicar:** Contextualizar o gargalo operacional (ex.: leads perdidos por digitação manual ou demora na triagem de chamados de suporte).

### 2.3. Objetivo
Declara de forma mensurável o que o workflow deve alcançar do início ao fim.
- **Como aplicar:** *"Projetar um workflow que receba dados via Webhook, higienize e valide os campos, prepare o registro e retorne uma confirmação estruturada em JSON."*

### 2.4. Público-Alvo
Define quem irá implementar, manter ou ser beneficiado pelo resultado do prompt.
- **Como aplicar:** Especificar se a explicação deve ser didática para estudantes/iniciantes no n8n ou estritamente técnica para desenvolvedores sêniores.

### 2.5. Ferramentas Envolvidas
Lista os sistemas, protocolos e nós nativos do n8n que devem ou podem ser utilizados.
- **Como aplicar:** Delimitar o uso de nós nativos (`Webhook`, `IF`, `Edit Fields (Set)`, `Code`, `AI Agent`, `Respond to Webhook`) para evitar dependências desnecessárias de serviços externos pagos.

### 2.6. Sequência de Execução
Descreve a ordem lógica das etapas do pipeline de dados.
- **Como aplicar:** Mapear o caminho passo a passo: *1. Recepção $\rightarrow$ 2. Normalização $\rightarrow$ 3. Validação Condicional $\rightarrow$ 4. Processamento/Enriquecimento $\rightarrow$ 5. Saída Síncrona*.

### 2.7. Regras de Negócio
Estabelece os critérios objetivos de validação, transformação e decisão.
- **Como aplicar:** Especificar quais campos são obrigatórios (`nome`, `email`), como validar o formato do e-mail, como padronizar strings (`.trim()`, `.toLowerCase()`) e quais categorias são permitidas na triagem.

### 2.8. Restrições
Define fronteiras explícitas do que a IA **não** pode fazer.
- **Como aplicar:** Proibir sintaxes descontinuadas (`$node["..."]`), proibir a inclusão de chaves de API reais ou segredos em JSON e proibir a invenção de parâmetros inexistentes nos nós.

### 2.9. Tratamento de Erros
Prevê o que deve acontecer quando a entrada é inválida ou quando um serviço/modelo externo falha.
- **Como aplicar:** Exigir ramificação *False* no nó `IF` retornando HTTP `400 Bad Request` / `422 Unprocessable Entity` com mensagem amigável, além de fallback determinístico caso o nó de IA falhe.

### 2.10. Formato de Saída
Determina a estrutura exata da resposta que a IA deve entregar.
- **Como aplicar:** Solicitar tabela de nós, diagrama em Mermaid, exemplos de payload de entrada/saída e bloco JSON compatível com o n8n.

### 2.11. Critérios de Validação
Lista o checklist pelo qual a resposta da IA será auditada antes de ir para produção.
- **Como aplicar:** Verificar se todos os nós citados nas conexões existem na lista de nós, se não há nomes duplicados e se os casos de teste positivos e negativos foram contemplados.

### 2.12. Iteração e Refinamento
Reconhece que o desenvolvimento de prompts é um ciclo contínuo de teste, inspeção de erros ("cicatrizes") e ajuste das instruções.
- **Como aplicar:** Ao notar que o LLM omitiu um campo ou usou expressão antiga, adicionar uma restrição negativa explícita na versão seguinte do prompt.

---

## 3. Tabela de Componentes do Prompt

A matriz abaixo resume os 12 componentes, a pergunta-chave que cada um responde e o risco de omiti-lo:

| # | Componente do Prompt | Pergunta-Chave Respondida | Risco de Omissão na Geração do Workflow |
| :---: | :--- | :--- | :--- |
| **01** | **Papel da IA (Persona)** | *Quem está projetando a solução?* | Respostas superficiais, sem rigor de engenharia ou padrões de mercado. |
| **02** | **Contexto** | *Qual é a dor de negócio atual?* | Solução desconectada da realidade operacional da equipe. |
| **03** | **Objetivo** | *Qual resultado concreto deve ser entregue?* | Fluxo incompleto que para no meio do caminho. |
| **04** | **Público-Alvo** | *Quem vai ler, importar ou manter o fluxo?* | Linguagem excessivamente hermética ou excessivamente rasa. |
| **05** | **Ferramentas Envolvidas** | *Quais nós e sistemas fazem parte do escopo?* | Sugestão de ferramentas pagas inacessíveis ou *Community Nodes* obsoletos. |
| **06** | **Sequência de Execução** | *Em que ordem os dados atravessam os nós?* | Grafo desorganizado, validando dados somente depois de tentar gravá-los. |
| **07** | **Regras de Negócio** | *O que torna um dado válido ou prioritário?* | Aceitação de payloads vazios, e-mails inválidos ou categorias inventadas. |
| **08** | **Restrições** | *O que é estritamente proibido fazer?* | Uso de sintaxe legada (`$node[...]`) ou exposição de tokens fixos no JSON. |
| **09** | **Tratamento de Erros** | *O que ocorre quando algo dá errado?* | Falhas silenciosas, timeouts no Webhook ou parada abrupta sem resposta. |
| **10** | **Formato de Saída** | *Como a resposta deve ser estruturada?* | Texto corrido confuso, impossível de importar ou documentar rapidamente. |
| **11** | **Critérios de Validação** | *Como provar que o workflow funciona?* | Ausência de payloads de teste para cenários de sucesso e erro. |
| **12** | **Iteração e Refinamento** | *Como evoluir o prompt após o primeiro teste?* | Repetição dos mesmos erros em futuras automações da equipe. |

---

## 4. Comparação Prática: Prompt Vago vs. Prompt Estruturado

Para visualizar o impacto direto da engenharia de prompts no planejamento de automações, observe os dois exemplos abaixo para o mesmo problema.

### ❌ Exemplo 1 — Antes (Prompt Vago e Incompleto)

```text
Crie um workflow no n8n que receba leads de um site e salve os dados. Se tiver IA, use também para classificar. Me dê o JSON.
```

**Por que este prompt falha?**
1. Não informa como os dados chegam (Webhook GET ou POST? Qual formato do body?).
2. Não define quais campos existem (`nome`, `email`, `telefone`, `origem`) nem quais são obrigatórios.
3. Não pede normalização (espaços extras, e-mails em caixa alta).
4. Não especifica o que fazer se o e-mail estiver inválido.
5. Pede armazenamento sem dizer se o usuário possui banco de dados configurado, gerando um JSON que falha imediatamente por falta de credenciais.

---

### ✅ Exemplo 2 — Depois (Prompt Estruturado e Profissional)

```text
[PAPEL]
Atue como um Engenheiro de Software Sênior especialista em automação de processos com n8n (v1.x/v2.x).

[CONTEXTO E OBJETIVO]
Nossa equipe comercial perde tempo copiando manualmente dados de formulários web e frequentemente recebe registros sem e-mail válido. Seu objetivo é projetar um workflow completo e didático no n8n para "Cadastro Automatizado de Leads", pronto para testes locais sem depender de credenciais externas obrigatórias.

[PÚBLICO-ALVO]
Estudantes e desenvolvedores iniciantes/intermediários em n8n que precisam entender a responsabilidade de cada nó.

[FERRAMENTAS E NÓS N8N]
Utilize exclusivamente nós nativos do n8n:
1. Webhook (n8n-nodes-base.webhook) — Recepção HTTP POST em /cadastro-leads com responseMode="responseNode".
2. Edit Fields / Set (n8n-nodes-base.set) — Higienização inicial (trim em strings, email em minúsculas).
3. IF (n8n-nodes-base.if) — Validação de presença de nome e formato de email contendo "@" e ".".
4. Edit Fields / Set (n8n-nodes-base.set) — Preparação do registro estruturado do lead (com protocolo único, timestamp ISO 8601 e status "registrado_demonstrativo").
5. Respond to Webhook (n8n-nodes-base.respondToWebhook) — Duas saídas distintas: HTTP 200 (Sucesso com resumo e notificação demonstrativa) e HTTP 400 (Erro detalhando campos inválidos).

[REGRAS DE NEGÓCIO E RESTRIÇÕES]
- Nome e e-mail são obrigatórios. Telefone, empresa e origem são opcionais (preencher com valor padrão se ausentes).
- Utilize apenas a sintaxe moderna de expressões do n8n ($json, $('Nome do Nó').item.json). NUNCA use $node["..."].
- NUNCA inclua credenciais, chaves de API ou tokens reais no JSON.
- Garanta que todos os nomes de nós na seção "connections" correspondam exatamente aos nomes definidos na lista "nodes".

[FORMATO DE SAÍDA]
1. Arquitetura do fluxo e explicação didática nó a nó (Entrada, Processamento, Saída e Erro).
2. Diagrama Mermaid (flowchart LR) representando os caminhos de sucesso e falha.
3. Bloco JSON válido do workflow exportável para o n8n.
4. Dois payloads JSON de teste (um válido e um inválido) e os resultados esperados.
```

---

## 5. Matriz de Problemas Encontrados ("Cicatrizes"), Causas e Melhorias

Durante os experimentos práticos com modelos de linguagem documentados neste repositório, foram mapeados os principais problemas gerados quando os prompts não possuem restrições adequadas:

| # | Problema Encontrado na Resposta da IA | Causa Provável no Prompt / Modelo | Melhoria Proposta e Aplicada no Prompt |
| :---: | :--- | :--- | :--- |
| **01** | Uso da sintaxe antiga `$node["Webhook"].json["email"]`. | Forte presença de tutoriais do n8n v0.x no corpus de treinamento geral dos LLMs. | Adicionar restrição explícita: *"Use exclusivamente a sintaxe moderna `$json` e `$('Nome').item.json`. É proibido usar `$node[...]`"*. |
| **02** | Sugestão de `Split In Batches` (loop manual) para processar um único item de Webhook. | O modelo confunde o motor de *item-lists* nativo do n8n com loops tradicionais de programação. | Instruir no prompt que o n8n itera listas nativamente e que loops só devem ser usados em paginação ou controle de *rate limit*. |
| **03** | Conexões quebradas no JSON (`connections` apontando para nomes de nós diferentes da lista `nodes`). | O modelo gera os nomes dos nós em português na lista `nodes`, mas referencia nomes em inglês no bloco `connections`. | Exigir no prompt: *"Mantenha correspondência exata (case-sensitive) entre a propriedade `name` de cada nó e as chaves do objeto `connections`"*. |
| **04** | Webhook respondendo antes do fim do processamento (`200 OK` vazio imediato mesmo quando o dado é inválido). | Omissão do parâmetro `responseMode: "responseNode"` no nó Webhook. | Especificar que o Webhook deve aguardar o nó `Respond to Webhook` em todas as ramificações (sucesso e erro). |
| **05** | Saída do agente de IA em texto livre quebrando o JSON de resposta da API. | Prompt interno do `AI Agent` sem definição de esquema JSON e sem etapa posterior de validação/sanitização. | Incluir um nó de validação/classificação pós-IA que verifica se a categoria e a prioridade pertencem à lista permitida e aplica fallback seguro. |
| **06** | Workflows impossíveis de testar localmente porque exigem credenciais pagas logo no meio do fluxo. | O prompt pediu integração direta com banco/CRM proprietário sem solicitar modo demonstrativo desacoplado. | Solicitar arquitetura com saída demonstrativa estruturada e documentar onde acoplar nós externos em produção. |

---

## 6. Alerta Crítico: Bons Prompts Não Substituem a Validação Técnica

> [!IMPORTANT]
> **Um prompt detalhado melhora drasticamente a orientação da IA, mas NÃO garante resultados 100% corretos sem validação empírica.**

Mesmo seguindo os 12 pilares, Modelos de Linguagem são sistemas probabilísticos sujeitos a erros sutis de sintaxe JSON, coordenadas de canvas sobrepostas ou expressões JavaScript com parênteses desbalanceados. Por essa razão, na engenharia de software assistida por IA, o prompt é sempre acompanhado por duas barreiras de verificação obrigatórias:

1. **Validação Estrutural Automatizada:** Executada neste projeto através do script [`tests/validar-workflows.py`](../tests/validar-workflows.py), que analisa programaticamente os arquivos `.json`, confirma a existência das chaves obrigatórias, verifica a integridade referencial de todas as conexões e audita a ausência de segredos.
2. **Testes Funcionais com Casos Positivos e Negativos:** Documentados em [`docs/07-validacao-e-testes.md`](./07-validacao-e-testes.md) e [`tests/casos-de-teste.md`](../tests/casos-de-teste.md), garantindo que o fluxo seja testado tanto com entradas perfeitas quanto com dados incompletos e fora do escopo.
