"""
=====================================================
Graph : Audit Graph
Purpose : Enterprise AI Auditor Workflow
=====================================================
"""

from langgraph.graph import (
    StateGraph,
    END
)

from backend.graph.state import (
    AuditState
)

from backend.agents.ocr_agent import (
    ocr_agent
)

from backend.agents.prompt_injection_agent import (
    prompt_injection_agent
)

from backend.agents.pii_agent import (
    pii_agent
)

from backend.agents.classifier_agent import (
    classifier_agent
)

from backend.agents.policy_agent import (
    policy_agent
)

from backend.agents.audit_agent_gpt import (
    audit_agent_gpt
)

from backend.agents.validator_agent import (
    validator_agent
)

from backend.agents.risk_agent import (
    risk_agent
)

from backend.agents.report_agent import (
    report_agent
)

from backend.agents.save_audit_agent import (
    save_audit_agent
)

from backend.agents.approval_agent import (
    approval_agent
)

# ==========================================
# Create Workflow
# ==========================================

workflow = StateGraph(
    AuditState
)


# ==========================================
# Nodes
# ==========================================

workflow.add_node(
    "ocr_agent",
    ocr_agent
)

workflow.add_node(
    "prompt_injection_agent",
    prompt_injection_agent
)

workflow.add_node(
    "pii_agent",
    pii_agent
)

workflow.add_node(
    "classifier_agent",
    classifier_agent
)

workflow.add_node(
    "policy_agent",
    policy_agent
)

workflow.add_node(
    "audit_agent",
    audit_agent_gpt
)

workflow.add_node(
    "validator_agent",
    validator_agent
)

workflow.add_node(
    "risk_agent",
    risk_agent
)

workflow.add_node(
    "approval_agent",
    approval_agent
)

workflow.add_node(
    "report_agent",
    report_agent
)

workflow.add_node(
    "save_audit_agent",
    save_audit_agent
)


# ==========================================
# Entry Point
# ==========================================

workflow.set_entry_point(
    "ocr_agent"
)


# ==========================================
# Workflow Edges
# ==========================================

workflow.add_edge(
    "ocr_agent",
    "prompt_injection_agent"
)

workflow.add_edge(
    "prompt_injection_agent",
    "pii_agent"
)

workflow.add_edge(
    "pii_agent",
    "classifier_agent"
)

workflow.add_edge(
    "classifier_agent",
    "policy_agent"
)

workflow.add_edge(
    "policy_agent",
    "audit_agent"
)

workflow.add_edge(
    "audit_agent",
    "validator_agent"
)

workflow.add_edge(
    "validator_agent",
    "risk_agent"
)

workflow.add_edge(
    "risk_agent",
    "approval_agent"
)

workflow.add_edge(
    "approval_agent",
    "report_agent"
)

workflow.add_edge(
    "report_agent",
    "save_audit_agent"
)

workflow.add_edge(
    "save_audit_agent",
    END
)


# ==========================================
# Compile Graph
# ==========================================

audit_graph = workflow.compile()