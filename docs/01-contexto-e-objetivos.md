# 01. Contexto e Objetivos do Projeto

> **Navegação:** [🏠 README Principal](../README.md) | [📚 Índice da Documentação](./README.md) | [Próximo: 02. Curadoria de Fontes ➡️](./02-curadoria-de-fontes.md)

---

## 1. Contexto do Desafio

Este projeto foi desenvolvido para o desafio técnico e educacional da **DIO (Digital Innovation One)** denominado:

> **Desafio Criativo: Planejando Automações com n8n Usando Apenas Bons Prompts**

No cenário atual de desenvolvimento de software e operações digitais (*DevOps / RevOps*), plataformas de orquestração de fluxos de trabalho baseadas em nós visuais — com destaque para o **n8n** — tornaram-se peças centrais para conectar APIs, bancos de dados, ferramentas de comunicação e Modelos de Linguagem de Grande Escala (LLMs).

Entretanto, antes de arrastar e conectar nós em uma tela (*canvas*), toda automação bem-sucedida nasce de um **planejamento claro de processo**. O desafio da DIO propõe exatamente exercitar essa competência analítica: utilizar técnicas estruturadas de **Engenharia de Prompts** para planejar, especificar regras de negócio, prever exceções e desenhar a arquitetura completa de uma automação no n8n assistida por Inteligência Artificial.

---

## 2. Problema que Será Resolvido

Equipes comerciais, de atendimento e de operações enfrentam diariamente dois gargalos críticos e interligados:

1. **Perda de Tempo e Erros em Tarefas Repetitivas Manuais:**
   - No **Cadastro de Leads**, formulários web enviam dados despadronizados (e-mails com espaços ou letras maiúsculas, telefones sem máscara, campos obrigatórios vazios). Quando o registro e o aviso à equipe comercial dependem de cópia manual para planilhas ou CRMs, leads quentes esfriam e registros corrompidos poluem a base.
   - Na **Triagem de Solicitações de Atendimento**, mensagens chegam por múltiplos canais misturando dúvidas comerciais, chamados urgentes de suporte técnico, questões financeiras e mensagens fora de escopo. A leitura e o encaminhamento puramente humanos geram filas de espera e priorização inadequada.

2. **Falha na Comunicação com Assistentes de IA ao Projetar Automações:**
   - Profissionais iniciantes frequentemente pedem à IA: *"Crie uma automação no n8n para cadastrar leads"*.
   - Como resultado de prompts vagos, os modelos geram respostas genéricas, sugerem sintaxes descontinuadas de versões antigas do n8n (como `$node["Nome"]` em vez de `$('Nome').item.json`), ignoram validações de campos obrigatórios, omitem caminhos de erro e não deixam claro o formato esperado do payload JSON.

---

## 3. Importância de Prompts Bem Estruturados

Na engenharia de automações assistida por IA, o **prompt funciona como um documento de especificação técnica executável**. Estruturar um bom prompt é determinante porque:

- **Elimina Ambiguidades de Arquitetura:** Define explicitamente qual é o gatilho (*Trigger*), quais são as transformações de dados, quais são os critérios de ramificação (*IF / Switch*) e como o fluxo deve responder ao sistema chamador.
- **Previne Alucinações Técnicas e Sintaxes Legadas:** Ao restringir a versão do n8n (v1.x+ / v2.x) e exigir nomes reais de nós nativos (`n8n-nodes-base.webhook`, `n8n-nodes-base.if`, `n8n-nodes-base.set`, `@n8n/n8n-nodes-langchain.agent`), evita-se que o modelo invente propriedades inexistentes.
- **Impõe Governança e Segurança desde o Design:** Obriga a especificação de regras de sanitização, tratamento de exceções (HTTP 400/422 para erros de validação, fallback para falhas de IA) e desacoplamento de credenciais.
- **Garante Reprodutibilidade:** Um template de prompt parametrizável permite que toda a equipe documente e projete novos workflows mantendo o mesmo padrão de qualidade.

---

## 4. Objetivos do Projeto

### 4.1. Objetivo Geral

Demonstrar, de ponta a ponta, como planejar, especificar e traduzir necessidades reais de negócio em **prompts estruturados de alta precisão** e em **workflows demonstrativos exportáveis para o n8n**, acompanhados de documentação técnica, diagramas explicativos, imagens didáticas nó a nó e validação estrutural automatizada.

### 4.2. Objetivos Específicos

1. **Mapear Tarefas Repetitivas:**Selecionar e detalhar dois cenários operacionais de alto impacto: **Cadastro Automatizado de Leads** (determinístico) e **Triagem Inteligente de Solicitações com IA** (cognitivo/híbrido).
2. **Construir uma Biblioteca de Prompts Reutilizáveis:** Desenvolver templates modulares para geração de documentação, arquitetura de workflows, *troubleshooting* de erros e o **Prompt Final do Desafio DIO**.
3. **Desenvolver Workflows JSON Válidos:** Criar arquivos `workflow.json` compatíveis com a estrutura de exportação do n8n, contendo nós reais, conexões íntegras, validações, normalização de dados e respostas estruturadas.
4. **Produzir Documentação Visual Didática:** Elaborar diagramas Mermaid (`.mmd`) e 15 ilustrações técnicas em PNG que expliquem visualmente a função de cada nó, a entrada/saída de dados e os desvios de erro para pessoas iniciantes.
5. **Validar Estruturalmente os Artefatos:** Implementar um script automatizado em Python (`tests/validar-workflows.py`) e uma suíte de casos de teste documentados (`tests/casos-de-teste.md`) para verificar a integridade dos fluxos e payloads.
6. **Versionar e Publicar com Boas Práticas:** Organizar o repositório seguindo padrões profissionais de Git, segurança da informação (zero exposição de segredos) e documentação em português brasileiro.

---

## 5. Público-Alvo

Este projeto foi desenhado para atender quatro perfis complementares:

- **Estudantes e Participantes de Bootcamps da DIO:** Que buscam uma referência prática, clara e visual de como resolver o desafio indo além do texto básico.
- **Iniciantes em Automação Low-Code / n8n:** Que precisam compreender como os dados entram por um *Webhook*, passam por nós de decisão (*IF*), são limpos no *Edit Fields (Set)* / *Code* e retornam respostas HTTP padronizadas.
- **Profissionais de Tecnologia e Analistas de Processos:** Que desejam adotar templates de engenharia de prompts para acelerar a especificação técnica e o diagnóstico de falhas em esteiras corporativas.
- **Avaliadores Técnicos e Recrutadores:** Que analisam a maturidade de engenharia de software, organização de documentação, clareza de comunicação e rigor de testes no portfólio.

---

## 6. Escopo do Projeto

### O que está incluído no escopo (In-Scope)
- Especificação completa do prompt mestre do desafio seguindo os 3 passos da DIO.
- Três templates adicionais de prompts reutilizáveis (conteúdo, design de workflow e troubleshooting).
- Dois workflows completos em formato JSON exportável pelo n8n (`01-cadastro-de-leads` e `02-triagem-inteligente-ia`).
- Payloads JSON de exemplo cobrindo casos válidos, incompletos e fora do escopo.
- Saídas demonstrativas autocontidas nos workflows (via `Respond to Webhook` e preparação de payload) para permitir inspeção e entendimento sem depender de contas pagas de terceiros.
- Validador estático em Python e documentação completa em 8 capítulos com diagramas e imagens didáticas.

### O que não está incluído no escopo (Out-of-Scope)
- Hospedagem de uma instância pública do n8n em nuvem rodando 24/7.
- Fornecimento de chaves de API reais (OpenAI, Slack, HubSpot, Postgres) dentro do repositório — por estrita conformidade com as regras de segurança.
- Persistência real em banco de dados de produção externo durante a validação estática local.

---

## 7. Diferenciação: Requisitos Originais da DIO vs. Extensões do Projeto

Para garantir total transparência técnica, a tabela abaixo diferencia o que era exigido originalmente na proposta básica do desafio da DIO e o que foi construído adicionalmente neste portfólio para comprovar a aplicação prática:

| Dimensão | Requisito Original do Desafio DIO | Extensão Implementada Neste Projeto |
| :--- | :--- | :--- |
| **Entrega Central** | Um arquivo Markdown contendo o prompt planejado nas 3 etapas (Definir automação, Adicionar contexto/regras, Montar prompt final). | Entregue integralmente em [`prompts/prompt-final-desafio-dio.md`](../prompts/prompt-final-desafio-dio.md), acrescido de 3 templates extras em [`prompts/`](../prompts/README.md). |
| **Cenários de Automação** | Planejamento textual de 1 fluxo de automação. | Planejamento e implementação em JSON de **2 workflows completos**: (1) Cadastro de Leads e (2) Triagem Inteligente com IA. |
| **Artefatos do n8n** | Apenas citação ou descrição textual dos nós sugeridos. | Arquivos `workflow.json` estruturalmente válidos, com parâmetros reais de nós n8n, expressões modernas e payloads de teste. |
| **Recursos Visuais** | Opcional / Não exigido obrigatoriamente. | **15 imagens PNG didáticas** geradas programaticamente em alta definição + **3 diagramas Mermaid** (`.mmd`) detalhando nó a nó. |
| **Testes e Qualidade** | Revisão manual do texto do prompt. | Script automatizado [`tests/validar-workflows.py`](../tests/validar-workflows.py) testando sintaxe JSON, grafos de conexão, unicidade de nós e ausência de credenciais. |
| **Documentação Técnica** | `README.md` explicando a entrega. | `README.md` principal completo + 8 capítulos técnicos em `docs/` (curadoria, engenharia de prompts, miniestudo, glossário, arquitetura, testes e guia de apresentação). |

---

## 8. Critérios de Sucesso e Entregáveis

O sucesso deste projeto é medido pela verificação objetiva dos seguintes entregáveis:

1. **Prompt Final Autossuficiente (`prompts/prompt-final-desafio-dio.md`):** Qualquer pessoa deve conseguir copiar o prompt final, colá-lo em um LLM moderno e obter uma especificação arquitetural completa e segura para o n8n.
2. **Integridade Estrutural dos Workflows (`workflows/`):** O script `python tests/validar-workflows.py` deve executar com código de saída `0` (100% de aprovação nas verificações sintáticas, de nós, conexões e segurança).
3. **Clareza Visual (`assets/`):** Todas as etapas de ambos os workflows devem possuir representação visual clara, em português brasileiro, sem textos ilegíveis e fielmente alinhada aos nomes dos nós nos arquivos JSON.
4. **Honestidade Técnica (`docs/07-validacao-e-testes.md`):** Distinção rigorosa entre o que foi validado estaticamente via script Python no ambiente local e o que depende de execução em uma instância ativa do n8n com credenciais configuradas pelo usuário.
