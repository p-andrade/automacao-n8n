# 🎨 Diretório de Recursos Visuais e Diagramas (`assets/`)

> **Navegação:** [🏠 README Principal](../README.md) | [🖼️ Galeria de Imagens (`assets/img/`)](./img/README.md) | [⚙️ Workflows n8n](../workflows/README.md)

---

## 📌 Visão Geral

Este diretório centraliza todos os **recursos visuais didáticos e diagramas técnicos** do projeto **Desafio DIO — Planejando Automações com n8n Usando Bons Prompts**.

Em conformidade com as diretrizes visuais de engenharia de documentação (Seção 11 do projeto), priorizamos **representações esquemáticas programáticas de alta precisão** (diagramas Mermaid `.mmd` e lâminas técnicas renderizadas em `.png` de alta definição `1400x780`), garantindo:
1. Textos 100% legíveis em **português brasileiro**.
2. Nomes dos nós estritamente idênticos aos definidos nos arquivos `workflow.json`.
3. Destaque visual claro para entradas (*Input JSON*), processamento, saídas (*Output JSON*), decisões condicionais (`True` / `False`) e tratamento de erros (`HTTP 400`).
4. Transparência ética e técnica: nenhuma imagem finge ser uma captura de tela de um serviço externo fictício.

---

## 📂 Estrutura do Diretório `assets/`

```text
assets/
├── README.md                          # Este guia geral de recursos visuais
├── diagrams/                          # Código-fonte textual dos diagramas Mermaid
│   ├── arquitetura-geral.mmd          # Relação entre Negócio -> Prompts -> Workflows -> Qualidade
│   ├── fluxo-cadastro-leads.mmd       # Grafo do Workflow 01 (Cadastro Automatizado de Leads)
│   └── fluxo-triagem-ia.mmd           # Grafo do Workflow 02 (Triagem Inteligente com IA)
└── img/                               # Imagens PNG renderizadas (1400x780 px)
    ├── README.md                      # Catálogo detalhado das 15 imagens PNG
    ├── banner-projeto.png             # Banner horizontal de abertura do repositório
    ├── arquitetura-geral.png          # Diagrama visual da arquitetura macro do projeto
    ├── 01-cadastro-leads/             # 6 imagens passo a passo do Workflow 01
    └── 02-triagem-inteligente-ia/     # 7 imagens passo a passo do Workflow 02
```

---

## 🔄 Como Atualizar Diagramas e Imagens Sem Quebrar Links

1. **Preservação de Nomes e Caminhos:** Todos os arquivos Markdown do repositório (`README.md`, `docs/*.md`, `workflows/*/README.md`) referenciam as imagens por caminhos relativos padronizados (ex.: `assets/img/banner-projeto.png`). Ao atualizar qualquer artefato visual, mantenha exatamente o mesmo nome de arquivo e extensão `.png`.
2. **Sincronia entre JSON, Mermaid e PNG:** Se você alterar o nome de um nó em `workflow.json`, atualize também o arquivo `.mmd` correspondente em `assets/diagrams/` e regenere a lâmina `.png` correspondente em `assets/img/`.
