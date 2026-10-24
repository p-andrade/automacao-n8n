# ⚙️ Workflows Demonstrativos n8n (`workflows/`)

> **Navegação:** [🏠 README Principal](../README.md) | [📚 Documentação Técnica](../docs/README.md) | [🤖 Biblioteca de Prompts](../prompts/README.md) | [🧪 Testes e Validação](../tests/README.md)

---

## 📌 Visão Geral

Este diretório contém os **dois workflows demonstrativos em formato JSON exportável pelo n8n** (desenvolvidos e validados na estrutura moderna do n8n `v2.42.7`), acompanhados de documentação ilustrada passo a passo e payloads JSON de teste.

| # | Diretório do Workflow | Objetivo Principal | Nós Utilizados | Dependência de Credencial Externa |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **[`01-cadastro-de-leads/`](./01-cadastro-de-leads/README.md)** | Receber dados de leads via Webhook `POST`, validar campos obrigatórios (`nome` e `email`), higienizar strings e retornar resposta estruturada (`HTTP 200` ou `HTTP 400`). | `Webhook`, `IF`, `Edit Fields (Set)` (2x), `Respond to Webhook` (2x) | **Nenhuma** (100% autocontido com nós nativos). |
| **02** | **[`02-triagem-inteligente-ia/`](./02-triagem-inteligente-ia/README.md)** | Receber solicitações de atendimento, normalizar dados, classificar com IA (`Comercial`, `Suporte técnico`, `Financeiro`, `Outros`), validar com *Guardrail* e retornar JSON auditado. | `Webhook`, `Edit Fields (Set)` (2x), `IF`, `AI Agent` + `OpenAI Chat Model`, `Code`, `Respond to Webhook` (2x) | **Opcional:** Requer credencial `OpenAI API` para inferência real em nuvem; inclui **fallback determinístico automático** caso executado sem credencial. |

---

## 📥 Como Importar os Arquivos JSON no n8n

Você pode importar qualquer um dos dois workflows em uma instância do **n8n Cloud** ou **n8n Self-Hosted** (via Docker ou CLI `npx n8n` / `n8n start`):

1. Abra o painel do seu **n8n** no navegador (por padrão, `http://localhost:5678` em execuções locais).
2. No menu lateral esquerdo, clique em **Workflows** e depois no botão **Add Workflow** (ou crie um workflow em branco).
3. No canto superior direito do editor (*canvas*), clique no ícone de menu **`⋮` (três pontos)** $\rightarrow$ **Import from File...**.
4. Selecione o arquivo desejado:
   - [`workflows/01-cadastro-de-leads/workflow.json`](./01-cadastro-de-leads/workflow.json)
   - [`workflows/02-triagem-inteligente-ia/workflow.json`](./02-triagem-inteligente-ia/workflow.json)
5. Alternativamente, você pode abrir o arquivo `workflow.json` em qualquer editor de texto, copiar todo o conteúdo (`Ctrl+C`) e colar diretamente na tela de edição do n8n (`Ctrl+V`).

---

## 🔐 Configuração de Credenciais e Cuidados de Segurança

> [!CAUTION]
> **Regra de Ouro de Segurança:** Nenhum arquivo `workflow.json` deste repositório contém chaves de API, senhas, tokens ou segredos reais. Jamais salve chaves privadas diretamente dentro de parâmetros de texto ou nós de código antes de exportar um workflow para o Git.

- **Para o Workflow 01 (`01-cadastro-de-leads`):** Não é necessário configurar nenhuma credencial. Ele utiliza apenas nós nativos de processamento local e responde diretamente no próprio Webhook.
- **Para o Workflow 02 (`02-triagem-inteligente-ia`):**
  - Se você desejar testar a classificação com o modelo `gpt-4o-mini` ao vivo na OpenAI, clique duas vezes no sub-nó **`Modelo OpenAI Chat`**, selecione **Create New Credential** e insira sua `API Key` no cofre seguro do n8n (criptografado por `N8N_ENCRYPTION_KEY`).
  - Se você **não** tiver uma chave da OpenAI disponível, **o workflow continuará funcionando**: graças ao parâmetro `continueOnFail: true` no nó `Agente IA de Triagem` e ao nó `Validar e Classificar Resposta` (`Code`), o fluxo detecta a ausência de resposta da API e aciona automaticamente o modo demonstrativo baseado em regras, identificando a saída com `"modo_execucao": "simulacao_demonstrativa_local"`.

---

## 🧪 Como Executar os Testes

### 1. Validação Estrutural e Lógica (Sem precisar subir servidor)
Na raiz do repositório, execute o script Python:
```powershell
python tests/validar-workflows.py
```
O validador verifica a sintaxe JSON, a integridade de todos os nós e conexões, a ausência de segredos e simula a lógica dos dois fluxos contra os payloads de exemplo.

### 2. Teste Interativo na Interface do n8n (Runtime)
1. Com o workflow importado e aberto no n8n, clique no botão **Test workflow** (ou **Listen for test event** dentro do nó `Webhook`).
2. Envie uma requisição HTTP `POST` para a **Test URL** exibida pelo n8n (por exemplo, `http://localhost:5678/webhook-test/cadastro-leads` ou `http://localhost:5678/webhook-test/triagem-ia`) usando os arquivos JSON de exemplo disponíveis em cada subpasta.
