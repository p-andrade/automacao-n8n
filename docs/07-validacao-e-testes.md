# 07. Validação, Qualidade e Relatório de Testes

> **Navegação:** [⬅️ 06. Arquitetura da Solução](./06-arquitetura-da-solucao.md) | [📚 Índice da Documentação](./README.md) | [Próximo: 08. Guia de Apresentação ➡️](./08-guia-de-apresentacao.md)

---

## 1. Critérios de Qualidade e Estratégia de Validação

Para garantir que os artefatos deste repositório sejam confiáveis, seguros e prontos para importação no **n8n**, a validação foi dividida em **três níveis claramente distintos**:

1. **Nível 1 — Validação Estrutural e de Segurança Automatizada (Executada via Python):**
   - Executada pelo script [`tests/validar-workflows.py`](../tests/validar-workflows.py) no ambiente local (Python `3.15.0`).
   - Verifica a existência de todos os arquivos JSON obrigatórios, validade sintática JSON, estrutura de exportação do n8n (`name`, `nodes`, `connections`), unicidade de IDs e nomes de nós, integridade referencial das conexões (nenhuma seta aponta para um nó inexistente), configuração de `Webhook` e `Respond to Webhook`, e auditoria de segurança (ausência de chaves de API ou tokens reais).

2. **Nível 2 — Simulação Lógica da Regra de Negócio e Guardrail (Executada via Python):**
   - Como o nó `Validar e Classificar Resposta` do Workflow 02 e as condições booleanas dos nós `IF` de ambos os workflows utilizam regras determinísticas bem definidas, executamos a validação lógica contra os payloads de exemplo (`exemplo-payload.json`, `entrada-valida.json`, `entrada-incompleta.json`, `entrada-fora-do-escopo.json`) para comprovar que as expressões e o algoritmo de fallback produzem exatamente as saídas documentadas.

3. **Nível 3 — Testes Funcionais E2E em Instância Ativa do n8n com Credencial Externa (Documentados como Pendentes de Ambiente do Usuário):**
   - Embora o binário `n8n` (`v2.42.7`) esteja instalado no ambiente, o disparo de chamadas HTTP em tempo real contra a API da OpenAI exige que o usuário configure sua própria chave privada (`OPENAI_API_KEY`) no cofre de credenciais do n8n. Em respeito absoluto à regra de **não inventar resultados de testes ou execuções externas**, esses cenários estão registrados na tabela abaixo com o status real **Pendente (Requer instância ativa / credencial do usuário)**, diferenciados dos testes estruturais e lógicos **Aprovados (Executados)**.

---

## 2. Matriz Completa de Testes (Estruturais, Funcionais e Negativos)

A tabela abaixo consolida todos os testes realizados e planejados para o projeto. Os campos de **Resultado Observado** dos testes `CT-01` a `CT-08` refletem a execução real do validador no ambiente local:

| ID do Teste | Cenário | Entrada | Resultado Esperado | Resultado Observado | Status | Observações |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **CT-01** | **Validação estrutural do Workflow 01 (Cadastro de Leads)** | `workflows/01-cadastro-de-leads/workflow.json` | JSON válido, 6 nós únicos, conexões íntegras (`Webhook` $\rightarrow$ `IF` $\rightarrow$ `Set` $\rightarrow$ `Respond`), sem credenciais expostas. | JSON válido; 6 nós verificados sem duplicatas; todas as conexões referenciam nós existentes; 0 segredos expostos. | ✅ **Executado — Aprovado** | Verificado automaticamente por `python tests/validar-workflows.py`. |
| **CT-02** | **Validação estrutural do Workflow 02 (Triagem IA)** | `workflows/02-triagem-inteligente-ia/workflow.json` | JSON válido, 8 nós únicos (incluindo `AI Agent` + sub-nó `lmChatOpenAi` conectado via `ai_languageModel`), conexões íntegras e sem chaves de API. | JSON válido; 8 nós verificados; conexão `ai_languageModel` íntegra; 0 segredos expostos. | ✅ **Executado — Aprovado** | Verificado automaticamente por `python tests/validar-workflows.py`. |
| **CT-03** | **Validação dos Payloads de Exemplo (Workflows 01 e 02)** | `exemplo-payload.json`, `entrada-valida.json`, `entrada-incompleta.json`, `entrada-fora-do-escopo.json` | Todos os 4 arquivos devem existir, ser JSONs válidos e conter os campos correspondentes ao seu cenário de teste. | Todos os 4 arquivos foram lidos e validados com sucesso pelo script Python. | ✅ **Executado — Aprovado** | Garante que os arquivos de teste prontos para uso não possuem erros de sintaxe. |
| **CT-04** | **Auditoria de Segurança (Zero Credenciais no Repositório)** | Todos os arquivos `workflow.json` e exemplos JSON | Nenhum token `sk-...`, senha, Bearer Token fixo ou chave privada deve existir nos arquivos versionados. | Varredura de expressões regulares e chaves de credenciais não encontrou nenhum segredo exposto. | ✅ **Executado — Aprovado** | Conformidade estrita com as regras 13 e 14 do projeto. |
| **CT-05** | **Simulação Lógica — Lead Válido (Caminho Feliz Workflow 01)** | `workflows/01-cadastro-de-leads/exemplo-payload.json` (`nome` e `email` preenchidos e válidos) | Condição do nó `Validar Dados do Lead` avaliada como `True`; e-mail normalizado em minúsculas; retorno HTTP 200. | Condição avaliada como `True`; dados normalizados corretamente na verificação lógica do validador. | ✅ **Executado — Aprovado** | Simulação estática da regra do nó `IF` e `Set`. |
| **CT-06** | **Simulação Lógica — Lead Inválido / Sem E-mail (Cenário Negativo Workflow 01)** | Payload com `{"nome": "João", "email": "email-invalido"}` (sem `@`) | Condição do nó `Validar Dados do Lead` avaliada como `False`; roteamento para `Responder Erro Validacao` (HTTP 400). | Condição avaliada como `False`; desvio confirmado para o ramo `main[1]` (`Responder Erro Validacao`). | ✅ **Executado — Aprovado** | Comprova o funcionamento do filtro *Fail-Fast*. |
| **CT-07** | **Simulação Lógica — Triagem com Entrada Válida e Guardrail (Workflow 02)** | `workflows/02-triagem-inteligente-ia/exemplos/entrada-valida.json` | Passa na verificação obrigatória (`True`); classifica na categoria `Suporte técnico` e prioridade `Alta` com estrutura controlada. | Verificação obrigatória `True`; lógica do nó `Validar e Classificar Resposta` retornou `categoria: "Suporte técnico"`, `prioridade: "Alta"`. | ✅ **Executado — Aprovado** | Validado o código de *guardrail/fallback* do nó `Code`. |
| **CT-08** | **Simulação Lógica — Triagem Incompleta e Fora do Escopo (Cenários Negativos Workflow 02)** | `entrada-incompleta.json` (sem email/mensagem) e `entrada-fora-do-escopo.json` | Entrada incompleta deve ser barrada no `IF` (`False` $\rightarrow$ HTTP 400). Entrada fora do escopo deve passar no `IF` (`True`) e ser classificada como `Outros` (`Baixa`). | `entrada-incompleta.json` barrada (`False`); `entrada-fora-do-escopo.json` classificada como `categoria: "Outros"`, `prioridade: "Baixa"`. | ✅ **Executado — Aprovado** | Comprova tratamento de dados faltantes e mensagens fora de domínio. |
| **CT-09** | **Execução HTTP ao vivo no servidor n8n (Workflow 01)** | `POST /webhook-test/cadastro-leads` com workflow ativo na interface do n8n | Receber resposta HTTP `200 OK` diretamente do motor web do n8n em execução. | **Não executado na sessão automatizada** (validação feita estaticamente em CT-01/CT-05). | ⏳ **Pendente (Execução Manual pelo Usuário)** | Requer iniciar `n8n start`, importar o JSON e clicar em *Listen for test event*. |
| **CT-10** | **Inferência Real com API OpenAI no Agente de IA (Workflow 02)** | `POST /webhook-test/triagem-ia` com credencial `OpenAI API` ativa no n8n | O nó `Agente IA de Triagem` consulta o modelo `gpt-4o-mini` na nuvem e retorna JSON validado com `status_validacao: "validado_ia"`. | **Não executado** por ausência intencional de chaves de API reais no ambiente. | ⏳ **Pendente (Requer Credencial OpenAI do Usuário)** | Sem credencial, o fluxo utiliza o modo demonstrativo seguro (`fallback_demonstrativo_regras`). |

---

## 3. Diferença entre Validade Estrutural JSON e Execução em Runtime no n8n

É fundamental destacar um ponto técnico importante para qualquer engenheiro de automação:

- **O que a Validação Estrutural (`validar-workflows.py`) Garante:**
  Garante que o arquivo `workflow.json` não está corrompido, respeita o esquema de exportação do n8n, possui todos os nós referenciados nas conexões, não tem nós órfãos ou duplicados, utiliza expressões modernas e as regras lógicas de filtragem/classificação funcionam conforme especificado.
- **O que Depende do Runtime do n8n:**
  A abertura de portas TCP locais (`5678`), o registro dinâmico dos Webhooks no banco SQLite interno do n8n e a autenticação OAuth/API Key contra servidores externos (como a OpenAI) só ocorrem quando o serviço do n8n está em execução ativa e autenticado pelo usuário final.

---

## 4. Limitações Conhecidas

1. **Ausência de Credenciais Externas Pré-configuradas:** Por determinação de segurança, o repositório não contém chaves de API. O Workflow 02 inclui um mecanismo explícito de contingência no nó `Validar e Classificar Resposta` para que o usuário possa estudar e testar a estrutura mesmo sem pagar por uma chave de LLM.
2. **Validação de Formato de E-mail Simplificada:** Os nós `IF` verificam a presença de `@` e `.` após higienização, o que cobre erros comuns de digitação em formulários, mas não substitui validação por envio de token de confirmação (*Double Opt-in*).
3. **Armazenamento Demonstrativo:** Os workflows retornam o payload pronto para persistência via `Respond to Webhook`, cabendo ao usuário conectar seu banco de dados (PostgreSQL, MySQL, Google Sheets) quando desejar retenção permanente.
