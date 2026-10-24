# 🤖 Biblioteca de Prompts Reutilizáveis para Automações n8n

> **Navegação:** [🏠 README Principal](../README.md) | [📚 Documentação Técnica](../docs/README.md) | [⚙️ Workflows n8n](../workflows/README.md)

---

## 📌 Visão Geral

Este diretório contém a **Biblioteca de Prompts Estruturados** do projeto **Desafio DIO — Planejando Automações com n8n Usando Bons Prompts**.

Cada arquivo foi projetado como um artefato de engenharia de software reutilizável, aplicando os 12 pilares documentados em [`docs/03-engenharia-de-prompts.md`](../docs/03-engenharia-de-prompts.md) (definição de papel, contexto, objetivo, público-alvo, ferramentas, sequência de execução, regras de negócio, restrições, tratamento de erros, formato de saída, critérios de validação e iteração).

> 🎯 **Procurando a entrega principal do Desafio da DIO?**  
> Acesse diretamente: **[`prompts/prompt-final-desafio-dio.md`](./prompt-final-desafio-dio.md)**

---

## 📋 Catálogo dos Prompts Disponíveis

| # | Arquivo | Finalidade Principal | Variáveis de Entrada (`{{...}}`) | Quando Utilizar |
| :---: | :--- | :--- | :--- | :--- |
| **01** | **[`prompt-final-desafio-dio.md`](./prompt-final-desafio-dio.md)** *(Entrega Principal DIO)* | Prompt completo, autossuficiente e pronto para copiar, estruturado nos **3 Passos oficiais da DIO** e preenchido com o cenário prático de **Cadastro Automatizado de Leads**. | Já preenchido com o caso completo (inclui guia rápido caso deseje trocar o processo). | Para submissão e avaliação na DIO ou para gerar imediatamente toda a proposta arquitetural e JSON do fluxo de Leads. |
| **02** | **[`prompt-design-workflow.md`](./prompt-design-workflow.md)** | Template especializado para solicitar à IA a arquitetura completa de qualquer workflow no n8n em 15 seções padronizadas (requisitos, nós, conexões, erros, testes e JSON). | `{{NOME_PROCESSO}}`, `{{VERSAO_N8N}}`, `{{GATILHO_ENTRADA}}`, `{{SISTEMAS_ENVOLVIDOS}}`, `{{REGRAS_NEGOCIO}}`, `{{CAMPOS_OBRIGATORIOS}}`, `{{DESTINO_SAIDA}}` | Sempre que precisar desenhar um novo workflow do zero garantindo compatibilidade com o n8n moderno. |
| **03** | **[`prompt-geracao-conteudo.md`](./prompt-geracao-conteudo.md)** | Template reutilizável para gerar documentação técnica, manuais operacionais, READMEs ilustrados e guias passo a passo de automações. | `{{TITULO_AUTOMACAO}}`, `{{PUBLICO_ALVO}}`, `{{NIVEL_TECNICO}}`, `{{LISTA_NOS_WORKFLOW}}`, `{{FONTES_OFICIAIS}}`, `{{FORMATO_DOCUMENTO}}` | Após criar ou modificar um workflow, para documentar o funcionamento de cada nó para a equipe ou portfólio. |
| **04** | **[`prompt-troubleshooting.md`](./prompt-troubleshooting.md)** | Template de diagnóstico e depuração (*debugging*) de erros em nós, expressões JavaScript/Python, Webhooks ou chamadas de API no n8n, com checklist de sanitização de segredos. | `{{VERSAO_N8N}}`, `{{NOME_E_TIPO_NO}}`, `{{DESCRICAO_PROBLEMA}}`, `{{MENSAGEM_ERRO}}`, `{{PAYLOAD_ENTRADA_ANONIMIZADO}}`, `{{SAIDA_ESPERADA}}`, `{{SAIDA_OBSERVADA}}` | Quando um workflow apresentar falha de execução, erro de expressão ou comportamento inesperado em testes. |

---

## 🛠️ Como Utilizar os Templates Parametrizáveis

1. **Escolha o template adequado** na tabela acima conforme sua necessidade (Planejamento DIO, Arquitetura de Novo Fluxo, Documentação ou Diagnóstico de Erro).
2. **Copie o bloco do prompt** contido no arquivo Markdown correspondente.
3. **Substitua os marcadores `{{VARIAVEL}}`** pelos dados reais do seu cenário (ou utilize diretamente o exemplo já preenchido incluído no final de cada arquivo).
4. **Revise o Checklist de Segurança** antes de enviar o prompt ao modelo de linguagem: **jamais** inclua tokens reais, chaves `sk-...`, senhas de banco de dados ou dados pessoais (CPF, e-mails reais de clientes) no texto enviado à IA.
5. **Valide o resultado gerado:** Caso o modelo produza um arquivo `workflow.json`, salve-o localmente e execute o validador [`tests/validar-workflows.py`](../tests/validar-workflows.py) antes de importar no n8n.
