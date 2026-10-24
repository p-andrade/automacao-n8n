# 08. Guia de Apresentação Técnica e Roteiro para Entrevistas

> **Navegação:** [⬅️ 07. Validação e Testes](./07-validacao-e-testes.md) | [📚 Índice da Documentação](./README.md) | [🏠 README Principal](../README.md)

---

## 1. Objetivo deste Guia

Este documento foi elaborado para servir como um **roteiro prático de apresentação (*pitch técnico*)** em entrevistas de emprego, avaliações de portfólio, revisões de código ou demonstrações na comunidade da **DIO**.

O foco deste roteiro não é apenas mostrar *"quais botões foram clicados no n8n"*, mas evidenciar o **raciocínio de engenharia de software**: como um problema ambíguo foi transformado em uma especificação rigorosa via Engenharia de Prompts, traduzido em workflows resilientes e auditado por testes automatizados.

---

## 2. Roteiro Estruturado de Apresentação (8 Etapas — 5 a 10 minutos)

### Etapa 1 — Contextualização do Desafio (1 min)
- **O que dizer:**
  > *"Este projeto nasceu do desafio da DIO 'Planejando Automações com n8n Usando Apenas Bons Prompts'. Em vez de entregar apenas um arquivo de texto isolado, decidi construir um portfólio completo de engenharia de automação: criei a biblioteca de prompts, desenvolvi dois workflows reais em JSON compatíveis com o n8n, desenhei diagramas e ilustrações passo a passo para iniciantes e escrevi um validador em Python para testar a integridade dos fluxos."*
- **Arquivo para mostrar na tela:** [`README.md`](../README.md) (exibindo o banner e a visão geral).

---

### Etapa 2 — O Problema de Negócio Escolhido (1 min)
- **O que dizer:**
  > *"Escolhi dois problemas reais e complementares que quase toda empresa enfrenta: primeiro, o **Cadastro Automatizado de Leads**, onde dados sujos ou sem e-mail válido vindos de landing pages poluem o CRM e atrasam o contato comercial; segundo, a **Triagem Inteligente de Solicitações com IA**, onde mensagens de clientes chegam misturadas e precisam ser classificadas automaticamente entre Comercial, Suporte técnico, Financeiro ou Outros, definindo prioridade e resumo."*
- **Arquivo para mostrar na tela:** [`docs/01-contexto-e-objetivos.md`](./01-contexto-e-objetivos.md).

---

### Etapa 3 — Como o Prompt Foi Estruturado (1,5 min)
- **O que dizer:**
  > *"Um erro comum ao usar IA para criar automações é fazer pedidos vagos, o que gera sintaxes depreciadas da versão 0.x do n8n (como `$node[...]`) e fluxos sem tratamento de erro. Para resolver isso, estruturei os prompts em 12 pilares — incluindo Persona de Arquiteto n8n, Contexto, Regras de Negócio, Restrições explícitas de versão e Formato de Saída controlado. No arquivo principal da entrega (`prompts/prompt-final-desafio-dio.md`), segui exatamente os 3 passos da DIO para que qualquer pessoa possa copiar o prompt e gerar a arquitetura completa."*
- **Arquivos para mostrar na tela:** [`prompts/prompt-final-desafio-dio.md`](../prompts/prompt-final-desafio-dio.md) e a tabela comparativa em [`docs/03-engenharia-de-prompts.md`](./03-engenharia-de-prompts.md).

---

### Etapa 4 — Por que Cada Nó Foi Escolhido nos Workflows (1,5 min)
- **O que dizer:**
  > *"Cada nó foi selecionado com base no princípio de responsabilidade única e usando apenas nós nativos do n8n para garantir portabilidade:*
  > - *O **Webhook** (`responseMode: responseNode`) recebe a chamada HTTP POST e mantém a conexão aberta até o processamento terminar.*
  > - *O nó **IF** atua como barreira Fail-Fast logo na entrada: se faltar nome, e-mail válido ou mensagem, ele desvia pelo ramo falso diretamente para um nó **Respond to Webhook** que devolve HTTP 400 Bad Request, poupando processamento e chamadas de API.*
  > - *O **Edit Fields (Set)** higieniza strings (`.trim()`, `.toLowerCase()`) e padroniza o contrato JSON.*
  > - *No segundo workflow, utilizei a arquitetura moderna de Cluster Nodes do n8n com o **AI Agent** conectado ao sub-nó **OpenAI Chat Model**, seguido por um nó **Code** que funciona como Guardrail determinístico."*
- **Arquivo para mostrar na tela:** [`docs/06-arquitetura-da-solucao.md`](./06-arquitetura-da-solucao.md).

---

### Etapa 5 — Como as Imagens e Diagramas Ajudam na Compreensão (1 min)
- **O que dizer:**
  > *"Como o público do repositório inclui iniciantes em automação, não basta entregar um arquivo JSON de centenas de linhas. Produzi diagramas Mermaid e 15 ilustrações técnicas em PNG que decompõem cada workflow nó por nó. Em cada README de workflow, a imagem de cada etapa vem acompanhada de seis respostas claras: o que acontece, qual nó é responsável, quais dados entram, quais saem, por que a etapa é necessária e o que ocorre se houver erro."*
- **Arquivos para mostrar na tela:** [`workflows/01-cadastro-de-leads/README.md`](../workflows/01-cadastro-de-leads/README.md) e [`workflows/02-triagem-inteligente-ia/README.md`](../workflows/02-triagem-inteligente-ia/README.md).

---

### Etapa 6 — Como os Testes e Validações Foram Realizados (1,5 min)
- **O que dizer:**
  > *"Bons prompts orientam a IA, mas engenharia de software exige verificação empírica. Criei o script `tests/validar-workflows.py` em Python, que verifica se os JSONs são sintaticamente válidos, se todos os nós possuem nomes únicos, se todas as setas em `connections` apontam para nós reais, se não há credenciais expostas e simula a lógica de validação contra payloads válidos, incompletos e fora do escopo."*
- **Arquivos para mostrar na tela:** [`tests/validar-workflows.py`](../tests/validar-workflows.py) e a matriz em [`docs/07-validacao-e-testes.md`](./07-validacao-e-testes.md).

---

### Etapa 7 — Quais Limitações Foram Identificadas com Transparência (1 min)
- **O que dizer:**
  > *"Fui rigoroso na transparência técnica: como um repositório público nunca deve conter chaves de API reais da OpenAI ou senhas de banco de dados, documentei claramente a diferença entre a validação estática/lógica executada localmente e a execução em runtime no n8n. Além disso, projetei o Workflow 02 com um fallback determinístico no nó `Code`: se a IA devolver uma categoria fora do padrão ou se o usuário testar o fluxo sem credencial da OpenAI, o workflow não quebra e retorna uma classificação segura identificada como modo demonstrativo."*

---

### Etapa 8 — Melhorias Futuras para Escala em Produção (1 min)
- **O que dizer:**
  > *"Para levar esses dois templates para um ambiente corporativo de alto volume, os próximos passos naturais são: (1) adicionar autenticação Header Auth ou JWT nos Webhooks; (2) acoplar um nó PostgreSQL ou CRM usando operação idempotente de Upsert por e-mail; (3) conectar um sub-workflow global com `Error Trigger` para alertas de observabilidade; e (4) adicionar memória conversacional e RAG (Vector Store) ao Agente de IA da triagem."*

---

## 3. Perguntas Frequentes em Entrevistas Técnicas (Q&A Rápido)

| Pergunta do Entrevistador | Resposta Técnica Recomendada |
| :--- | :--- |
| **"Por que você colocou um nó `Code` depois do `AI Agent` no Workflow 02?"** | *"Porque LLMs são probabilísticos. Mesmo pedindo JSON no prompt de sistema, o modelo pode envolver a resposta em blocos markdown ` ```json ` ou inventar uma categoria fora da lista permitida. O nó `Code` atua como um *Guardrail* de esquema: faz o parse seguro com `try/catch`, valida os valores permitidos e aplica fallback determinístico se necessário."* |
| **"Por que você usou `Respond to Webhook` em vez da resposta padrão do nó Webhook?"** | *"Porque a resposta padrão (`onReceived`) devolve `200 OK` imediatamente antes de saber se os dados são válidos. Com `responseMode: responseNode` e nós `Respond to Webhook` separados, consigo devolver `400 Bad Request` quando faltam campos obrigatórios e `200 OK` com o protocolo gerado quando tudo dá certo."* |
| **"Qual o maior erro que uma IA comete ao gerar workflows para o n8n?"** | *"Usar a sintaxe legada `$node['Nome'].json['campo']` da versão 0.x em vez da sintaxe moderna `$('Nome').item.json.campo`, ou criar nomes de nós na lista `nodes` que não batem com as chaves do objeto `connections`. Por isso incluí restrições explícitas contra isso nos meus templates de prompt e no validador Python."* |
