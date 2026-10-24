# 🧪 Diretório de Testes e Validação Automatizada (`tests/`)

> **Navegação:** [🏠 README Principal](../README.md) | [📊 Relatório de Validação (`docs/07`)](../docs/07-validacao-e-testes.md) | [📋 Casos de Teste (`casos-de-teste.md`)](./casos-de-teste.md)

---

## 📌 Visão Geral

Este diretório reúne as ferramentas e especificações de **Garantia de Qualidade (QA)** dos workflows e exemplos JSON desenvolvidos para o projeto **Desafio DIO — Planejando Automações com n8n Usando Bons Prompts**.

### Arquivos deste Diretório
- **[`validar-workflows.py`](./validar-workflows.py):** Script automatizado em Python (sem dependências externas de terceiros, utilizando apenas a biblioteca padrão `json`, `re`, `sys`, `pathlib`) que audita os arquivos `workflow.json` e os payloads de exemplo.
- **[`casos-de-teste.md`](./casos-de-teste.md):** Catálogo detalhado de casos de teste positivos, negativos, caminhos alternativos e falhas de integração para ambos os cenários.

---

## ▶️ Como Executar o Validador Automatizado

A partir da raiz do repositório, execute no terminal (PowerShell, CMD ou Bash):

```powershell
python tests/validar-workflows.py
```

### O que o Script Verifica Automaticamente:
1. **Existência dos Arquivos:** Confirma que `workflows/01-cadastro-de-leads/workflow.json`, `workflows/02-triagem-inteligente-ia/workflow.json` e todos os 4 arquivos JSON de exemplo existem.
2. **Validade Sintática JSON:** Garante que nenhum arquivo contém erros de formatação JSON.
3. **Estrutura Exportável do n8n:** Verifica a presença de `name`, `nodes`, `connections` e coordenadas `[x, y]`.
4. **Unicidade de Nós:** Impede nomes ou IDs de nós duplicados.
5. **Integridade Referencial das Conexões:** Confirma que toda seta declarada em `connections` parte de um nó existente e aponta para um nó existente (incluindo conexões `main` e `ai_languageModel`).
6. **Auditoria de Segurança:** Varre todos os JSONs garantindo ausência de credenciais acopladas ou chaves de API (`sk-...`, `ghp_...`, `Bearer ...`) e proíbe a sintaxe depreciada `$node[...]`.
7. **Simulação Lógica:** Testa as regras condicionais e de classificação contra os payloads válidos, incompletos e fora do escopo.
