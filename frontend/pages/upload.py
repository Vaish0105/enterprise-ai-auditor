"""
=====================================================
Page : Upload Center
Purpose : Document Upload + Full Audit Workflow
=====================================================
"""

import gradio as gr

from backend.graph.audit_graph import (
    audit_graph
)


# Process uploaded document
# Run complete AI audit workflow
def process_uploaded_document(
        file
):

    if file is None:

        return {
            "error":
            "No file uploaded"
        }

    try:

        result = audit_graph.invoke(
            {
                "file_path":
                file.name
            }
        )

        return {

            "document_type":
            result.get(
                "document_type"
            ),

            "risk_score":
            result.get(
                "risk_score"
            ),

            "violations":
            result.get(
                "violations"
            ),

            "validation_status":
            result.get(
                "validation_status"
            ),

            "approval_required":
            result.get(
                "approval_required"
            ),

            "approval_status":
            result.get(
                "approval_status"
            )
        }

    except Exception as e:

        return {

            "error":
            str(e)
        }


# Build upload page
# Upload and audit documents
def build_upload_page():

    with gr.Column():

        gr.Markdown(
            "# Upload Center"
        )

        uploaded_file = gr.File(
            label="Upload Document"
        )

        process_button = gr.Button(
            "Process Document"
        )

        result_markdown = gr.Markdown()

    process_button.click(
        fn=process_and_format,
        inputs=uploaded_file,
        outputs=result_markdown
)

def format_audit_result(result):

    risk_score = result.get(
        "risk_score",
        0
    )

    if risk_score >= 80:

        risk_level = "🔴 HIGH"

    elif risk_score >= 50:

        risk_level = "🟡 MEDIUM"

    else:

        risk_level = "🟢 LOW"

    violations = result.get(
        "violations",
        []
    )

    violation_text = ""

    for v in violations:

        if isinstance(v, dict):

            violation_text += f"""
###  {v.get('violation')}

**Policy**
{v.get('policy')}

**Evidence**
{v.get('evidence')}

---
"""

        else:

            violation_text += f" {v}\n\n"

    summary = f"""
# Audit Summary

### Document Type
{result.get('document_type')}

### Risk Level
{risk_level}

### Risk Score
{risk_score}

### Approval Required
{result.get('approval_required')}

### Approval Status
{result.get('approval_status')}

### Violations

{violation_text}
"""

    return summary

def process_and_format(
        file
):

    result = process_uploaded_document(
        file
    )

    return format_audit_result(
        result
    )