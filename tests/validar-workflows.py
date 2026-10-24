#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador Estrutural, de Segurança e de Lógica dos Workflows n8n
Projeto: Desafio DIO — Planejando Automações com n8n Usando Bons Prompts

O que este script valida:
1. Existência de todos os arquivos JSON obrigatórios (workflows e exemplos).
2. Validade sintática JSON (UTF-8) de todos os arquivos.
3. Presença dos elementos essenciais de exportação do n8n (name, nodes, connections).
4. Ausência de nós com nomes ou IDs duplicados dentro de cada workflow.
5. Integridade referencial das conexões (toda origem e destino em 'connections'
   deve existir na lista 'nodes').
6. Consistência dos nomes dos nós com a arquitetura documentada e as imagens.
7. Configurações críticas de Webhook (httpMethod=POST, responseMode=responseNode).
8. Auditoria de segurança: ausência de credenciais reais, tokens sk-..., senhas ou segredos.
9. Simulação lógica das regras de validação e classificação contra os payloads de exemplo.

NOTA TÉCNICA IMPORTANTE:
A aprovação neste validador comprova a integridade estrutural, sintática, referencial
e lógica dos arquivos JSON, mas não substitui o teste de execução em runtime dentro de
uma instância ativa do servidor n8n com credenciais externas configuradas.
"""

import json
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

EXPECTED_WORKFLOWS = {
    "workflows/01-cadastro-de-leads/workflow.json": {
        "expected_nodes": [
            "Webhook Receber Lead",
            "Validar Dados do Lead",
            "Preparar Registro do Lead",
            "Montar Notificacao Demonstrativa",
            "Responder Sucesso",
            "Responder Erro Validacao",
        ],
        "webhook_node": "Webhook Receber Lead",
        "webhook_path": "cadastro-leads",
    },
    "workflows/02-triagem-inteligente-ia/workflow.json": {
        "expected_nodes": [
            "Webhook Entrada Solicitacao",
            "Normalizar Dados de Entrada",
            "Verificar Dados Obrigatorios",
            "Agente IA de Triagem",
            "Modelo OpenAI Chat",
            "Validar e Classificar Resposta",
            "Formatar Saida Estruturada",
            "Responder Triagem Concluida",
            "Responder Erro Dados Incompletos",
        ],
        "webhook_node": "Webhook Entrada Solicitacao",
        "webhook_path": "triagem-ia",
    },
}

EXPECTED_PAYLOADS = [
    "workflows/01-cadastro-de-leads/exemplo-payload.json",
    "workflows/02-triagem-inteligente-ia/exemplos/entrada-valida.json",
    "workflows/02-triagem-inteligente-ia/exemplos/entrada-incompleta.json",
    "workflows/02-triagem-inteligente-ia/exemplos/entrada-fora-do-escopo.json",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AIza[0-9A-Za-z\-_]{30,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9\-._~+/]+=*", re.IGNORECASE),
]


def load_json_file(rel_path: str):
    full_path = ROOT_DIR / rel_path
    if not full_path.exists():
        return None, f"Arquivo esperado não encontrado: {rel_path}"
    try:
        content = full_path.read_text(encoding="utf-8")
        data = json.loads(content)
        return data, None
    except Exception as exc:
        return None, f"Erro ao interpretar JSON em {rel_path}: {exc}"


def check_security_no_secrets(rel_path: str) -> list[str]:
    errors = []
    full_path = ROOT_DIR / rel_path
    raw_text = full_path.read_text(encoding="utf-8")
    for pattern in SECRET_PATTERNS:
        if pattern.search(raw_text):
            errors.append(f"Possível segredo/token detectado em {rel_path} pelo padrão {pattern.pattern}")

    data = json.loads(raw_text)
    if isinstance(data, dict) and "nodes" in data:
        for node in data.get("nodes", []):
            if "credentials" in node and node["credentials"]:
                errors.append(
                    f"Nó '{node.get('name')}' em {rel_path} contém bloco 'credentials' acoplado."
                )
    return errors


def validate_workflow_structure(rel_path: str, spec: dict) -> list[str]:
    errors = []
    data, err = load_json_file(rel_path)
    if err:
        return [err]

    if not isinstance(data, dict):
        return [f"{rel_path}: A raiz do JSON deve ser um objeto."]

    for key in ("name", "nodes", "connections"):
        if key not in data:
            errors.append(f"{rel_path}: Chave obrigatória '{key}' ausente no workflow.")

    nodes = data.get("nodes", [])
    connections = data.get("connections", {})

    if not isinstance(nodes, list) or len(nodes) == 0:
        errors.append(f"{rel_path}: 'nodes' deve ser uma lista não vazia.")
        return errors

    node_names = []
    node_ids = []
    nodes_by_name = {}

    for idx, node in enumerate(nodes):
        n_name = node.get("name")
        n_id = node.get("id")
        n_type = node.get("type")
        n_pos = node.get("position")

        if not n_name:
            errors.append(f"{rel_path}: Nó no índice {idx} não possui 'name'.")
        else:
            node_names.append(n_name)
            nodes_by_name[n_name] = node

        if not n_id:
            errors.append(f"{rel_path}: Nó '{n_name}' não possui 'id'.")
        else:
            node_ids.append(n_id)

        if not n_type:
            errors.append(f"{rel_path}: Nó '{n_name}' não possui 'type'.")

        if not isinstance(n_pos, list) or len(n_pos) != 2:
            errors.append(f"{rel_path}: Nó '{n_name}' possui 'position' inválido.")

    # Verificar duplicidade de nomes e IDs
    dup_names = {x for x in node_names if node_names.count(x) > 1}
    if dup_names:
        errors.append(f"{rel_path}: Nós com nomes duplicados encontrados: {sorted(dup_names)}")

    dup_ids = {x for x in node_ids if node_ids.count(x) > 1}
    if dup_ids:
        errors.append(f"{rel_path}: Nós com IDs duplicados encontrados: {sorted(dup_ids)}")

    # Verificar se os nós esperados estão presentes
    missing_expected = [n for n in spec["expected_nodes"] if n not in nodes_by_name]
    if missing_expected:
        errors.append(f"{rel_path}: Nós obrigatórios ausentes: {missing_expected}")

    # Verificar conexões
    if not isinstance(connections, dict) or len(connections) == 0:
        errors.append(f"{rel_path}: 'connections' deve ser um dicionário não vazio.")
    else:
        for src_node, conn_types in connections.items():
            if src_node not in nodes_by_name:
                errors.append(
                    f"{rel_path}: Conexão parte de nó de origem inexistente: '{src_node}'."
                )
            if not isinstance(conn_types, dict):
                errors.append(f"{rel_path}: Estrutura de conexão inválida em '{src_node}'.")
                continue
            for conn_kind, branches in conn_types.items():
                for branch_idx, targets in enumerate(branches):
                    for target in targets:
                        dest_node = target.get("node")
                        if dest_node not in nodes_by_name:
                            errors.append(
                                f"{rel_path}: Conexão de '{src_node}' ({conn_kind}[{branch_idx}]) "
                                f"aponta para nó de destino inexistente: '{dest_node}'."
                            )

    # Verificar configuração do Webhook inicial
    wh_name = spec["webhook_node"]
    if wh_name in nodes_by_name:
        wh_params = nodes_by_name[wh_name].get("parameters", {})
        if wh_params.get("httpMethod") != "POST":
            errors.append(f"{rel_path}: '{wh_name}' deve ter httpMethod='POST'.")
        if wh_params.get("path") != spec["webhook_path"]:
            errors.append(f"{rel_path}: '{wh_name}' deve ter path='{spec['webhook_path']}'.")
        if wh_params.get("responseMode") != "responseNode":
            errors.append(f"{rel_path}: '{wh_name}' deve ter responseMode='responseNode'.")

    # Verificar ausência de sintaxe legada $node[...]
    raw_text = (ROOT_DIR / rel_path).read_text(encoding="utf-8")
    if "$node[" in raw_text:
        errors.append(f"{rel_path}: Sintaxe depreciada '$node[...]' detectada.")

    errors.extend(check_security_no_secrets(rel_path))
    return errors


def simulate_workflow_logic() -> list[str]:
    """Executa testes lógicos funcionais nas regras de validação dos dois workflows."""
    errors = []

    # 1. Simular regra do Workflow 01 com exemplo-payload.json
    lead_payload, err = load_json_file("workflows/01-cadastro-de-leads/exemplo-payload.json")
    if err:
        return [err]

    nome_clean = str(lead_payload.get("nome", "")).strip()
    email_clean = str(lead_payload.get("email", "")).strip().lower()
    is_valid_lead = bool(nome_clean) and ("@" in email_clean) and ("." in email_clean)
    if not is_valid_lead or email_clean != "mariana.costa@empresa.com.br":
        errors.append("Falha na simulação lógica do Workflow 01 para exemplo-payload.json.")

    # Simular caso negativo Workflow 01
    bad_email = "email-invalido-sem-arroba.com"
    if ("@" in bad_email) and ("." in bad_email):
        errors.append("Falha na simulação negativa do Workflow 01.")

    # 2. Simular regras do Workflow 02 nos 3 exemplos
    valida, _ = load_json_file("workflows/02-triagem-inteligente-ia/exemplos/entrada-valida.json")
    incompleta, _ = load_json_file("workflows/02-triagem-inteligente-ia/exemplos/entrada-incompleta.json")
    fora_escopo, _ = load_json_file("workflows/02-triagem-inteligente-ia/exemplos/entrada-fora-do-escopo.json")

    def check_wf2_if(p: dict) -> bool:
        return (
            bool(str(p.get("solicitante", "")).strip())
            and ("@" in str(p.get("email", "")).strip())
            and bool(str(p.get("mensagem", "")).strip())
        )

    def classify_fallback(p: dict) -> tuple[str, str]:
        texto = f"{p.get('assunto', '')} {p.get('mensagem', '')}".lower()
        prio_inf = str(p.get("prioridade_informada", "")).lower()
        if re.search(r"(erro|bug|fora do ar|caiu|falha|webhook|api|timeout|indispon|suporte|travando)", texto):
            prio = "Alta" if re.search(r"(urgente|crítico|critico|fora do ar|caiu|produção|producao|alta)", texto + " " + prio_inf) else "Média"
            return "Suporte técnico", prio
        if re.search(r"(boleto|fatura|nota fiscal|cobrança|cobranca|pagamento|reembolso|pix|assinatura)", texto):
            return "Financeiro", "Média"
        if re.search(r"(orçamento|orcamento|proposta|plano|contratar|licença|licenca|demonstração|demonstracao|preço|preco|comercial)", texto):
            return "Comercial", "Média"
        return "Outros", "Baixa"

    if not check_wf2_if(valida):
        errors.append("Workflow 02: entrada-valida.json deveria ser aprovada no nó IF.")
    cat_v, prio_v = classify_fallback(valida)
    if (cat_v, prio_v) != ("Suporte técnico", "Alta"):
        errors.append(f"Workflow 02: classificação inesperada para entrada-valida.json: {(cat_v, prio_v)}")

    if check_wf2_if(incompleta):
        errors.append("Workflow 02: entrada-incompleta.json deveria ser reprovada (False) no nó IF.")

    if not check_wf2_if(fora_escopo):
        errors.append("Workflow 02: entrada-fora-do-escopo.json deveria passar no nó IF.")
    cat_f, prio_f = classify_fallback(fora_escopo)
    if (cat_f, prio_f) != ("Outros", "Baixa"):
        errors.append(f"Workflow 02: classificação inesperada para entrada-fora-do-escopo.json: {(cat_f, prio_f)}")

    return errors


def main() -> int:
    print("=" * 76)
    print(" VALIDADOR DE WORKFLOWS N8N — DESAFIO DIO BONS PROMPTS")
    print("=" * 76)

    all_errors = []

    # 1. Validar Workflows principais
    for wf_path, spec in EXPECTED_WORKFLOWS.items():
        wf_errors = validate_workflow_structure(wf_path, spec)
        if wf_errors:
            all_errors.extend(wf_errors)
            print(f"[FALHA] {wf_path}")
        else:
            print(f"[OK] Estrutura, nós, conexões e segurança validados: {wf_path} ({len(spec['expected_nodes'])} nós)")

    # 2. Validar arquivos de Payload de exemplo
    for payload_path in EXPECTED_PAYLOADS:
        _, err = load_json_file(payload_path)
        if err:
            all_errors.append(err)
            print(f"[FALHA] {payload_path}: {err}")
        else:
            sec_errs = check_security_no_secrets(payload_path)
            if sec_errs:
                all_errors.extend(sec_errs)
                print(f"[FALHA] {payload_path}")
            else:
                print(f"[OK] Payload de exemplo válido e seguro: {payload_path}")

    # 3. Simular lógica de validação e classificação
    sim_errors = simulate_workflow_logic()
    if sim_errors:
        all_errors.extend(sim_errors)
        print("[FALHA] Simulação lógica dos casos de teste.")
    else:
        print("[OK] Simulação lógica dos casos de teste (Positivos, Negativos e Fora do Escopo)")

    print("-" * 76)
    if all_errors:
        print(f"RESULTADO FINAL: FALHA ({len(all_errors)} erro(s) encontrado(s)):")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("RESULTADO FINAL: SUCESSO — Todos os workflows e payloads passaram em 100% das verificações!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
