"""
=====================================================
Page : Audit Details
Purpose : View individual audit
=====================================================
"""

import json

import gradio as gr

from backend.database.audit_details_repository import (
    get_audit_details
)


def view_audit(
        audit_id
):

    record = get_audit_details(
        audit_id
    )

    if not record:

        return "Audit not found"

    violations = json.loads(
        record.violations
    )

    violation_text = ""

    for item in violations:

        violation_text += f"""
###  {item.get('violation')}

**Policy**

{item.get('policy')}

**Evidence**

{item.get('evidence')}

---

"""

    return f"""
# Audit #{record.audit_id}

## Document Type

{record.document_type}

## Risk Score

{record.risk_score}

## Validation Status

{record.validation_status}

## Approval Status

{record.approval_status}

## Approval Required

{record.approval_required}

## Violations

{violation_text}
"""


def build_audit_details_page():

    with gr.Column():

        gr.Markdown(
            "# Audit Details Viewer"
        )

        audit_id = gr.Number(
            label="Audit ID",
            value=1
        )

        view_button = gr.Button(
            "View Audit"
        )

        result = gr.Markdown()

        view_button.click(
            fn=view_audit,
            inputs=audit_id,
            outputs=result
        )