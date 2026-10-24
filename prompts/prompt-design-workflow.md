# 🏗️ Template de Prompt: Design e Arquitetura de Workflows no n8n

> **Navegação:** [⬅️ Geração de Conteúdo](./prompt-geracao-conteudo.md) | [📋 Catálogo de Prompts](./README.md) | [Próximo: Troubleshooting ➡️](./prompt-troubleshooting.md)

---

## 1. Objetivo e Finalidade

Este template é especializado em **Arquitetura de Soluções e Design de Workflows para o n8n**. Ele instrui a Inteligência Artificial a atuar como um Arquiteto de Integrações Sênior e a entregar uma especificação completa em **15 pontos obrigatórios**, incluindo o arquivo JSON exportável compatível com a versão informada do n8n, sem inventar parâmetros ou propriedades inexistentes.

---

## 2. Variáveis de Entrada (`{{...}}`)

| Variável | Descrição | Exemplo |
| :--- | :--- | :--- |
| `{{NOME_PROCESSO}}` | Nome da automação a ser projetada. | `Triagem Inteligente de Solicitações com IA` |
| `{{VERSAO_N8N}}` | Versão alvo do n8n instalada no ambiente. | `2.42.7 (série 1.x / 2.x moderna)` |
| `{{OBJETIVO_NEGOCIO}}` | Resultado esperado pela área de negócio. | `Receber chamados via Webhook, classificar com IA em 4 categorias e retornar JSON validado.` |
| `{{SISTEMAS_ENVOLVIDOS}}` | Sistemas ou nós permitidos na arquitetura. | `Nativos do n8n (Webhook, Set, IF, AI Agent + OpenAI Chat Model, Code, Respond to Webhook)` |
| `{{REGRAS_E_VALIDACOES}}` | Critérios de aceitação, campos obrigatórios e domínios. | `Solicitante, email (@) e mensagem obrigatórios. Categorias: Comercial, Suporte técnico, Financeiro, Outros.` |

---

## 3. Template Especializado em Arquitetura n8n (Pronto para Copiar)

```markdown
# PROMPT: ARQUITETURA E DESIGN DE WORKFLOW N8N

## PAPEL E DIRETRIZES DE ENGENHARIA
Atue como um Arquiteto de Software Sênior especialista em automação de processos com n8n (versão de referência: {{VERSAO_N8N}}).
Sua missão é projetar a arquitetura completa e gerar o workflow para o processo: **{{NOME_PROCESSO}}**.

- **Objetivo de Negócio:** {{OBJETIVO_NEGOCIO}}
- **Sistemas e Nós Envolvidos:** {{SISTEMAS_ENVOLVIDOS}}
- **Regras de Negócio e Validações:** {{REGRAS_E_VALIDACOES}}

## REGRAS DE COMPATIBILIDADE E SEGURANÇA (OBRIGATÓRIAS)
1. Verifique a compatibilidade dos nós com a versão {{VERSAO_N8N}} do n8n. NÃO invente tipos de nós (`type`), propriedades ou parâmetros que não existam oficialmente nos pacotes `n8n-nodes-base` ou `@n8n/n8n-nodes-langchain`.
2. Utilize exclusivamente a sintaxe moderna de expressões (`$json.campo`, `$('Nome do Nó').item.json.campo`). É estritamente proibido usar a sintaxe depreciada `$node["Nome"]`.
3. NUNCA inclua chaves de API reais, senhas ou tokens no JSON. Caso um nó exija autenticação externa, referencie apenas um placeholder de credencial e documente sua configuração.
4. Quando o workflow precisar ser testado sem dependências externas pagas, implemente uma saída demonstrativa clara (ex.: via `Respond to Webhook`) ou fallback determinístico, sem fingir que dados foram gravados em sistemas externos não conectados.

## ESTRUTURA DE SAÍDA OBRIGATÓRIA (15 SEÇÕES)
Sua resposta deve conter exatamente os 15 itens abaixo, numerados nesta ordem:

1. **Objetivo do Processo:** Descrição executiva do que a automação realiza do início ao fim.
2. **Requisitos Funcionais (RF):** Lista numerada das capacidades obrigatórias do fluxo (entrada, transformação, decisão e saída).
3. **Requisitos Não Funcionais (RNF):** Critérios de segurança, desempenho, idempotência, portabilidade e tolerância a falhas.
4. **Sistemas Envolvidos:** Tabela listando os serviços/protocolos integrados e o papel de cada um.
5. **Sequência de Execução:** Passo a passo ordenado do caminho feliz (*happy path*) e dos desvios condicionais, acompanhado de um diagrama Mermaid (`flowchart LR`).
6. **Nome e Tipo de Cada Nó:** Tabela contendo Ordem, Nome Exato do Nó (em português), Tipo Técnico (`type`), Versão (`typeVersion`) e Responsabilidade.
7. **Configurações Relevantes:** Explicação dos parâmetros críticos de cada nó (ex.: `httpMethod`, `path`, `responseMode`, condições do `IF`, expressões do `Edit Fields (Set)` e prompt de sistema do `AI Agent`).
8. **Entradas e Saídas Esperadas:** Contratos JSON de exemplo para o payload recebido no gatilho e para os payloads devolvidos no final.
9. **Regras de Negócio:** Detalhamento das regras de higienização, obrigatoriedade de campos e classificação.
10. **Caminhos Alternativos:** Como o workflow lida com campos opcionais ausentes ou solicitações fora do escopo padrão.
11. **Tratamento de Erros:** Como o fluxo responde a payloads inválidos (ex.: HTTP 400) e como evita quebras caso um modelo de IA ou serviço externo falhe (ex.: `continueOnFail` + validação/fallback).
12. **Credenciais Necessárias:** Lista de credenciais requeridas no cofre do n8n para operação completa em produção e como o modo demonstrativo funciona sem elas.
13. **Testes:** Matriz de casos de teste positivos, negativos e de borda com entradas e resultados esperados.
14. **JSON de Workflow (`workflow.json`):** Bloco de código JSON sintaticamente válido, completo e pronto para importação no n8n, garantindo que todos os nomes em `connections` correspondam exatamente aos nomes em `nodes`.
15. **Documentação para Importação:** Instruções passo a passo para importar o JSON no n8n, ativar o modo de teste e disparar requisições `curl` ou Postman.
```

---

## 4. Exemplo de Uso Aplicado ao Projeto

Este template foi utilizado diretamente como base para especificar os dois workflows deste repositório:
- **Workflow 01:** [`workflows/01-cadastro-de-leads/workflow.json`](../workflows/01-cadastro-de-leads/workflow.json)
- **Workflow 02:** [`workflows/02-triagem-inteligente-ia/workflow.json`](../workflows/02-triagem-inteligente-ia/workflow.json)
