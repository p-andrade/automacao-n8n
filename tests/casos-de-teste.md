# 📋 Especificação de Casos de Teste — Workflows 01 e 02

> **Navegação:** [⬅️ Diretório `tests/`](./README.md) | [📊 Resultados Observados (`docs/07`)](../docs/07-validacao-e-testes.md) | [🏠 README Principal](../README.md)

---

## 📌 Visão Geral

Este documento registra os **casos de teste positivos, negativos, caminhos alternativos e cenários de falha de integração** projetados para validar o **Workflow 01 (Cadastro Automatizado de Leads)** e o **Workflow 02 (Triagem Inteligente de Solicitações com IA)**.

---

## 1. Cenário 01 — Cadastro Automatizado de Leads (`workflows/01-cadastro-de-leads/`)

### Caso 1.1 — Lead Válido com Espaços e E-mail em Caixa Alta (Teste Positivo)
- **Arquivo de Entrada:** [`workflows/01-cadastro-de-leads/exemplo-payload.json`](../workflows/01-cadastro-de-leads/exemplo-payload.json)
- **Payload Enviado:**
  ```json
  {
    "nome": "  Mariana Costa  ",
    "email": "MARIANA.COSTA@empresa.com.br ",
    "telefone": "(11) 98765-4321",
    "empresa": "TechNova Soluções Digitais",
    "origem": "Landing Page Desafio DIO",
    "interesse": "Implantação de Automações com n8n e IA"
  }
  ```
- **Caminho Esperado no Grafo:** `Webhook Receber Lead` $\rightarrow$ `Validar Dados do Lead` (`True`) $\rightarrow$ `Preparar Registro do Lead` $\rightarrow$ `Montar Notificacao Demonstrativa` $\rightarrow$ `Responder Sucesso`.
- **Saída Esperada:** Código `HTTP 200 OK`, `nome: "Mariana Costa"`, `email: "mariana.costa@empresa.com.br"`, `status_processamento: "registrado_demonstrativo"`.

---

### Caso 1.2 — Lead com Campos Opcionais Ausentes (Caminho Alternativo Positivo)
- **Payload Enviado:**
  ```json
  {
    "nome": "Lucas Ferreira",
    "email": "lucas@startup.io"
  }
  ```
- **Caminho Esperado no Grafo:** Ramo `True` completo.
- **Saída Esperada:** Código `HTTP 200 OK`, preenchendo automaticamente os opcionais com valores padrão seguros (`telefone: "Não informado"`, `empresa: "Não informada"`, `origem: "Direto / Não especificada"`, `interesse: "Geral"`).

---

### Caso 1.3 — Lead Sem Nome Preenchido (Teste Negativo — Campo Obrigatório Ausente)
- **Payload Enviado:**
  ```json
  {
    "nome": "   ",
    "email": "contato@empresa.com.br"
  }
  ```
- **Caminho Esperado no Grafo:** `Webhook Receber Lead` $\rightarrow$ `Validar Dados do Lead` (`False`) $\rightarrow$ `Responder Erro Validacao`.
- **Saída Esperada:** Código `HTTP 400 Bad Request` com `"status": "erro_validacao"`.

---

### Caso 1.4 — Lead com E-mail em Formato Inválido (Teste Negativo — Formato Incorreto)
- **Payload Enviado:**
  ```json
  {
    "nome": "Pedro Souza",
    "email": "pedro.souza.empresa.com"
  }
  ```
- **Caminho Esperado no Grafo:** `Webhook Receber Lead` $\rightarrow$ `Validar Dados do Lead` (`False` por ausência de `@`) $\rightarrow$ `Responder Erro Validacao`.
- **Saída Esperada:** Código `HTTP 400 Bad Request` detalhando os dados recebidos e a ação recomendada.

---

## 2. Cenário 02 — Triagem Inteligente de Solicitações com IA (`workflows/02-triagem-inteligente-ia/`)

### Caso 2.1 — Solicitação Técnica Crítica Completa (Teste Positivo Principal)
- **Arquivo de Entrada:** [`workflows/02-triagem-inteligente-ia/exemplos/entrada-valida.json`](../workflows/02-triagem-inteligente-ia/exemplos/entrada-valida.json)
- **Payload Enviado:** Relato de erro 503 e timeout no Webhook em produção há 20 minutos.
- **Caminho Esperado no Grafo:** `Webhook Entrada Solicitacao` $\rightarrow$ `Normalizar Dados de Entrada` $\rightarrow$ `Verificar Dados Obrigatorios` (`True`) $\rightarrow$ `Agente IA de Triagem` $\rightarrow$ `Validar e Classificar Resposta` $\rightarrow$ `Formatar Saida Estruturada` $\rightarrow$ `Responder Triagem Concluida`.
- **Saída Esperada:** Código `HTTP 200 OK`, `categoria: "Suporte técnico"`, `prioridade: "Alta"`, `resumo` e `justificativa` preenchidos.

---

### Caso 2.2 — Solicitação com E-mail Inválido e Mensagem Vazia (Teste Negativo)
- **Arquivo de Entrada:** [`workflows/02-triagem-inteligente-ia/exemplos/entrada-incompleta.json`](../workflows/02-triagem-inteligente-ia/exemplos/entrada-incompleta.json)
- **Payload Enviado:** E-mail sem `@` (`"email-invalido-sem-arroba.com"`) e `mensagem: ""`.
- **Caminho Esperado no Grafo:** `Webhook Entrada Solicitacao` $\rightarrow$ `Normalizar Dados de Entrada` $\rightarrow$ `Verificar Dados Obrigatorios` (`False`) $\rightarrow$ `Responder Erro Dados Incompletos`.
- **Saída Esperada:** Código `HTTP 400 Bad Request` bloqueando a chamada antes de acionar o modelo de IA.

---

### Caso 2.3 — Solicitação Fora do Escopo de Negócio (Caminho Alternativo)
- **Arquivo de Entrada:** [`workflows/02-triagem-inteligente-ia/exemplos/entrada-fora-do-escopo.json`](../workflows/02-triagem-inteligente-ia/exemplos/entrada-fora-do-escopo.json)
- **Payload Enviado:** Convite para patrocínio de feira gastronômica e parceria cultural.
- **Caminho Esperado no Grafo:** Caminho `True` completo; classificado na categoria residual controlada.
- **Saída Esperada:** Código `HTTP 200 OK`, `categoria: "Outros"`, `prioridade: "Baixa"`.

---

### Caso 2.4 — Falha de Integração da API de IA ou Ausência de Credencial (Teste de Resiliência / Fallback)
- **Condição Simulada:** O nó `Agente IA de Triagem` falha por falta de chave da OpenAI ou retorna uma categoria inventada fora da lista permitida (ex.: `"Categoria Inventada"`).
- **Comportamento Esperado:** Como `Agente IA de Triagem` possui `continueOnFail: true`, a execução prossegue para o nó `Validar e Classificar Resposta` (`Code`), que rejeita a saída inválida e aplica a regra determinística de fallback, retornando `HTTP 200 OK` com `status_validacao: "validado_fallback_regras"`.
