# 📚 Documentação Técnica — Planejando Automações com n8n Usando Bons Prompts

Bem-vindo ao diretório central de documentação técnica do projeto **Desafio DIO — Planejando Automações com n8n Usando Bons Prompts**. Este acervo foi projetado sob princípios de design instrucional e engenharia de software para conduzir estudantes, iniciantes e profissionais desde a concepção de um problema operacional até a modelagem, validação e apresentação de workflows reais no **n8n** (versão 2.42.7 verificada no ambiente).

---

## 🗺️ Trilha de Leitura Recomendada

A documentação está organizada em uma sequência lógica e progressiva de **8 capítulos principais**:

| Ordem | Documento | Propósito Principal | Público Recomendado |
| :---: | :--- | :--- | :--- |
| **01** | [01-contexto-e-objetivos.md](./01-contexto-e-objetivos.md) | Contextualiza o desafio da DIO, o problema de negócio, escopo, entregáveis e diferencia o requisito original das extensões práticas implementadas. | Todos os perfis |
| **02** | [02-curadoria-de-fontes.md](./02-curadoria-de-fontes.md) | Apresenta o catálogo auditável de fontes primárias oficiais (`docs.n8n.io`, `docs.github.com`), datas de acesso, critérios de seleção e limitações. | Pesquisadores e Arquitetos |
| **03** | [03-engenharia-de-prompts.md](./03-engenharia-de-prompts.md) | Detalha a metodologia de construção de prompts para automação (12 pilares), comparativos *Antes vs. Depois* e matriz de mitigação de alucinações. | Engenheiros de Prompt e Devs |
| **04** | [04-miniestudo-final.md](./04-miniestudo-final.md) | Miniestudo completo *"Da intenção ao workflow: como transformar bons prompts em automações n8n"* cobrindo os dois cenários práticos de ponta a ponta. | Estudantes e Analistas |
| **05** | [05-glossario.md](./05-glossario.md) | Dicionário técnico em tabela com 22 termos essenciais de automação, n8n, IA e Git/GitHub, acompanhados de exemplos práticos e relação com o projeto. | Iniciantes e Estudantes |
| **06** | [06-arquitetura-da-solucao.md](./06-arquitetura-da-solucao.md) | Documenta a arquitetura técnica, contratos de dados JSON, pontos de validação, caminhos de erro e diagramas Mermaid sincronizados com os workflows. | Desenvolvedores e Arquitetos |
| **07** | [07-validacao-e-testes.md](./07-validacao-e-testes.md) | Registra a estratégia de qualidade, validação estática automatizada (`validar-workflows.py`), matriz de casos de teste executados e pendentes, e limitações. | QA e Engenheiros de Software |
| **08** | [08-guia-de-apresentacao.md](./08-guia-de-apresentacao.md) | Roteiro estruturado (*pitch técnico*) para defender as decisões arquiteturais e de prompting deste projeto em entrevistas técnicas e avaliações de portfólio. | Candidatos e Profissionais |

---

## 🔗 Conexão com os Demais Diretórios do Repositório

- **Quer ir direto para a entrega principal da DIO?** Acesse [`prompts/prompt-final-desafio-dio.md`](../prompts/prompt-final-desafio-dio.md).
- **Quer consultar os templates reutilizáveis de prompts?** Acesse [`prompts/README.md`](../prompts/README.md).
- **Quer inspecionar ou importar os workflows JSON no n8n?** Acesse [`workflows/README.md`](../workflows/README.md).
- **Quer visualizar os diagramas e ilustrações didáticas?** Acesse [`assets/README.md`](../assets/README.md).
- **Quer executar o script de validação estrutural em Python?** Acesse [`tests/README.md`](../tests/README.md).

---

## 🗂️ Histórico e Preservação de Artefatos Anteriores

Em respeito às boas práticas de evolução de repositório, os rascunhos da fase exploratória anterior (`03-mini-estudo-n8n.md`, `04-glossario.md`, `05-prompts-e-cicatrizes.md` e `06-conclusoes-e-aprendizados.md`) tiveram todo o seu conteúdo técnico revisado, expandido e consolidado nos 8 documentos canônicos listados na tabela acima.
