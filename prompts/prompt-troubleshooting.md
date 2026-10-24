# 🛠️ Template de Prompt: Troubleshooting e Diagnóstico de Erros no n8n

> **Navegação:** [⬅️ Design de Workflow](./prompt-design-workflow.md) | [📋 Catálogo de Prompts](./README.md) | [Próximo: Prompt Final Desafio DIO ➡️](./prompt-final-desafio-dio.md)

---

## 1. Objetivo e Finalidade

Este template foi desenvolvido para orientar engenheiros e estudantes a diagnosticarem rapidamente **falhas de execução, erros de expressão JavaScript/Python, problemas de pareamento de itens (*item pairing*) ou respostas inesperadas de Webhooks e Agentes de IA no n8n**.

---

## 2. Protocolo Obrigatório de Sanitização de Segredos (Antes de Usar)

> [!CAUTION]
> **NUNCA compartilhe credenciais reais, tokens ou dados pessoais sensíveis (LGPD) em prompts enviados a Modelos de Linguagem.**

Antes de colar qualquer log de erro, cabeçalho HTTP ou payload JSON no template abaixo, execute este checklist:
1. **Remova Tokens e Chaves de API:** Substitua qualquer chave `sk-...`, `Bearer eyJ...`, `x-api-key` ou senha por `"<TOKEN_REMOVIDO>"`.
2. **Anonimize Dados Pessoais (PII):** Substitua nomes reais de clientes, CPFs, telefones e e-mails privados por dados fictícios equivalentes (ex.: `"cliente@exemplo.com.br"`, `"(11) 90000-0000"`).
3. **Oculte URLs Internas Privadas:** Substitua endereços de servidores internos ou IPs privados por `"https://meu-servidor-n8n.exemplo.com"`.

---

## 3. Template de Diagnóstico (Pronto para Copiar)

```markdown
# PROMPT: DIAGNÓSTICO E TROUBLESHOOTING DE WORKFLOW N8N

## PAPEL DA IA
Atue como um Engenheiro de Confiabilidade de Site (SRE) e Especialista Sênior em Debugging de Workflows no n8n.

## DADOS DO INCIDENTE (SANITIZADOS)

1. **Descrição do Problema:**
   {{DESCRICAO_DO_PROBLEMA}}

2. **Mensagem de Erro Exata / Stack Trace:**
   ```text
   {{MENSAGEM_DE_ERRO}}
   ```

3. **Nó Afetado (Nome e Tipo `type`):**
   {{NO_AFETADO}}

4. **Versão do n8n e Ambiente de Execução:**
   {{VERSAO_N8N}} (Ex.: n8n v2.42.7 Local / Docker / Cloud)

5. **Configurações Relevantes do Nó Afetado (Expressões ou Parâmetros):**
   ```json
   {{CONFIGURACOES_DO_NO}}
   ```

6. **Entrada Recebida pelo Nó (Payload JSON Anonimizado):**
   ```json
   {{ENTRADA_RECEBIDA}}
   ```

7. **Saída Esperada:**
   ```json
   {{SAIDA_ESPERADA}}
   ```

8. **Saída Observada (Atual):**
   ```json
   {{SAIDA_OBSERVADA}}
   ```

## TAREFA DE DIAGNÓSTICO SOLICITADA
Com base exclusivamente nos dados acima e na documentação oficial do n8n ({{VERSAO_N8N}}), estruture sua resposta nas seguintes seções:

1. **Hipóteses de Causa Raiz (Ordenadas por Probabilidade):**
   - Explique tecnicamente por que o erro ocorreu (ex.: diferença entre `$json.body.campo` e `$json.campo` no Webhook, quebra de *item pairing*, erro de sintaxe de expressão ou JSON malformado retornado por IA).
2. **Correção Proposta Passo a Passo:**
   - Apresente a expressão exata corrigida (usando apenas sintaxe moderna `$json` ou `$('Nome do Nó').item.json`) ou o ajuste de parâmetro no nó.
3. **Prevenção de Falhas Futuras (Defesa em Profundidade):**
   - Como evitar que entradas inesperadas causem esse mesmo erro novamente (ex.: uso de coalescência nula `??`, validação prévia no nó `IF` ou tratamento `try/catch` no nó `Code`).
4. **Testes de Regressão Recomendados:**
   - Forneça pelo menos 2 payloads JSON de teste (um caso válido e um caso de borda/negativo) para confirmar que a correção resolveu o bug sem quebrar o restante do workflow.
```

---

## 4. Exemplo Prático Preenchido (Caso Real de Troubleshooting no n8n)

Abaixo está um exemplo completo de preenchimento das variáveis para diagnosticar um erro clássico em Webhooks do n8n:

- **`{{DESCRICAO_DO_PROBLEMA}}`**: O nó `IF` sempre avalia o e-mail como vazio quando envio dados via `curl POST`, embora o JSON enviado contenha o campo `email`.
- **`{{MENSAGEM_DE_ERRO}}`**: Sem erro de parada, mas o fluxo desvia sempre para a saída `false` (`Responder Erro Validacao`).
- **`{{NO_AFETADO}}`**: `Validar Dados do Lead` (`n8n-nodes-base.if`, v2).
- **`{{VERSAO_N8N}}`**: `n8n v2.42.7`.
- **`{{CONFIGURACOES_DO_NO}}`**: Expressão usada: `={{ $json.email }}` em vez de considerar que o Webhook aninha o payload enviado via POST dentro de `body` (`$json.body.email`).
- **`{{ENTRADA_RECEBIDA}}`**: `{"headers": {"content-type": "application/json"}, "body": {"nome": "Teste", "email": "teste@exemplo.com"}}`.
- **`{{SAIDA_ESPERADA}}`**: Condição `true` avaliada com sucesso.
- **`{{SAIDA_OBSERVADA}}`**: Condição `false` porque `$json.email` era `undefined`.
- **Correção Aplicada nos Nossos Workflows:** Utilização de expressão híbrida resiliente `={{ ($json.body?.email ?? $json.email ?? '').toString().trim() }}`, que funciona tanto quando o payload vem encapsulado em `body` pelo Webhook quanto quando é testado diretamente em objetos planos.
