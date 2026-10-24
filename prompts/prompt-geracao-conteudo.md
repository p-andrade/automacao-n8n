# 📝 Template de Prompt: Geração de Documentação Técnica de Automações

> **Navegação:** [⬅️ Catálogo de Prompts](./README.md) | [🏠 README Principal](../README.md) | [Próximo: Design de Workflow ➡️](./prompt-design-workflow.md)

---

## 1. Objetivo e Finalidade

Este template reutilizável foi desenvolvido para orientar Modelos de Linguagem (LLMs) a produzirem **documentação técnica clara, didática, precisa e auditável** para workflows construídos no **n8n**. Ele evita textos superficiais ou genéricos, exigindo explicações nó a nó, tabelas de contratos de dados, diagramas em Mermaid e avisos explícitos sobre credenciais e limitações.

---

## 2. Campos Parametrizáveis (`{{...}}`)

Antes de enviar o template à IA, preencha as seguintes variáveis:

| Variável | Descrição | Exemplo de Preenchimento |
| :--- | :--- | :--- |
| `{{TITULO_AUTOMACAO}}` | Nome do workflow ou processo automatizado. | `Triagem Inteligente de Solicitações com IA` |
| `{{CONTEXTO_NEGOCIO}}` | Dor operacional resolvida pela automação. | `Atendimento recebe mensagens misturadas sem classificação prévia de setor e urgência.` |
| `{{PUBLICO_ALVO}}` | Quem lerá a documentação gerada. | `Estudantes iniciantes em n8n e analistas de suporte técnico.` |
| `{{VERSAO_N8N}}` | Versão de referência do n8n. | `n8n v2.42.7 (compatível com v1.x+)` |
| `{{LISTA_NOS_WORKFLOW}}` | Sequência dos nós presentes no fluxo. | `Webhook -> Edit Fields (Set) -> IF -> AI Agent -> Code -> Respond to Webhook` |
| `{{FONTES_OFICIAIS}}` | URLs oficiais que devem embasar a terminologia. | `https://docs.n8n.io/workflows/ e https://docs.n8n.io/advanced-ai/` |

---

## 3. Template Reutilizável (Pronto para Copiar)

```markdown
# PROMPT: GERAÇÃO DE DOCUMENTAÇÃO TÉCNICA PARA WORKFLOW N8N

## 1. PAPEL DA IA
Atue como um Engenheiro de Software Sênior, Especialista em Documentação Técnica (Technical Writer) e Designer Instrucional com domínio profundo da plataforma n8n ({{VERSAO_N8N}}).

## 2. CONTEXTO
Preciso documentar de forma profissional, didática e auditável a automação "{{TITULO_AUTOMACAO}}".
Contexto de negócio: {{CONTEXTO_NEGOCIO}}
Sequência de nós implementada no workflow: {{LISTA_NOS_WORKFLOW}}

## 3. OBJETIVO
Redigir um documento técnico completo em Markdown que permita a qualquer pessoa do público-alvo compreender o objetivo do fluxo, importar o arquivo JSON no n8n, entender o papel exato de cada nó, configurar variáveis/credenciais com segurança e executar testes positivos e negativos.

## 4. PÚBLICO-ALVO
{{PUBLICO_ALVO}}
Utilize português brasileiro claro, técnico e acessível, explicando siglas ou jargões quando aparecerem pela primeira vez.

## 5. FONTES E REFERÊNCIAS
Baseie toda a nomenclatura técnica e sintaxe nas seguintes referências oficiais:
- {{FONTES_OFICIAIS}}
Não invente URLs, nomes de propriedades ou recursos que não existam na documentação oficial do n8n.

## 6. ESTRUTURA OBRIGATÓRIA DA RESPOSTA
Organize o documento exatamente com as seguintes seções em Markdown:
1. **Título e Visão Geral:** Resumo executivo do problema resolvido e do valor gerado.
2. **Arquitetura e Diagrama Mermaid:** Fluxograma (`flowchart LR`) representando todos os nós, decisões (`IF`) e caminhos de sucesso e erro.
3. **Pré-requisitos e Segurança:** Versão do n8n, credenciais necessárias (se houver) e cuidados para nunca expor chaves de API.
4. **Detalhamento Passo a Passo de Cada Nó:** Para cada nó de `{{LISTA_NOS_WORKFLOW}}`, responda obrigatoriamente:
   - O que acontece nesta etapa?
   - Qual nó e tipo (`type`) no n8n é responsável?
   - Quais dados entram (Input JSON)?
   - Quais dados saem (Output JSON)?
   - Por que essa etapa é necessária?
   - O que ocorre se houver erro nesta etapa?
5. **Guia de Importação e Execução no n8n:** Passo a passo numerado para importar o `workflow.json`.
6. **Casos de Teste (Positivos e Negativos):** Exemplos de payloads JSON de entrada e respostas esperadas.
7. **Limitações Conhecidas e Próximos Passos:** Diferenciação honesta entre modo demonstrativo e ambiente de produção.

## 7. RESTRIÇÕES
- NUNCA utilize a sintaxe legada `$node["Nome"]` (descontinuada desde o n8n v1.0). Utilize exclusivamente `$json` e `$('Nome do Nó').item.json`.
- NUNCA inclua chaves de API reais, senhas ou tokens nos exemplos. Use marcadores claros como `<SUA_CREDENTIAL_CONFIGURADA_NO_N8N>`.
- Não afirme que uma integração externa foi testada em produção se o fluxo estiver em modo demonstrativo.

## 8. CRITÉRIOS DE QUALIDADE E FORMATO FINAL
- Entregue o resultado em um único bloco Markdown bem formatado, utilizando tabelas, alertas GitHub (`> [!NOTE]`, `> [!IMPORTANT]`), blocos de código `json` e diagrama `mermaid` sem erros de sintaxe.
```

---

## 4. Exemplo Prático de Uso Preenchido

Caso você deseje gerar a documentação do nosso **Workflow 01 (Cadastro de Leads)**, basta preencher as variáveis do final da seção 2 como mostrado abaixo:

```text
{{TITULO_AUTOMACAO}} = Workflow 01: Cadastro Automatizado de Leads
{{CONTEXTO_NEGOCIO}} = Receber dados de formulários web via Webhook, barrar e-mails inválidos ou nomes vazios, higienizar os campos e retornar confirmação HTTP estruturada.
{{PUBLICO_ALVO}} = Estudantes da DIO e iniciantes em automação com n8n.
{{VERSAO_N8N}} = n8n v2.42.7
{{LISTA_NOS_WORKFLOW}} = 1. Webhook Receber Lead -> 2. Validar Dados do Lead (IF) -> 3. Preparar Registro do Lead (Set) -> 4. Montar Notificacao Demonstrativa (Set) -> 5. Responder Sucesso / 6. Responder Erro Validacao
{{FONTES_OFICIAIS}} = https://docs.n8n.io/workflows/, https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/
```
