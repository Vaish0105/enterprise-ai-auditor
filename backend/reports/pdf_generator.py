"""
=====================================================
Module : PDF Generator
Purpose : Generate audit PDF reports
=====================================================
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  # type: ignore[import]

from reportlab.lib.styles import getSampleStyleSheet  # type: ignore[import]


def generate_audit_pdf(
        state,
        output_file
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    content.append(

        Paragraph(
            "Enterprise AI Auditor Report",
            styles["Title"]
        )

    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(

        Paragraph(
            f"Document Type: {state.get('document_type')}",
            styles["BodyText"]
        )

    )

    content.append(

        Paragraph(
            f"Risk Score: {state.get('risk_score')}",
            styles["BodyText"]
        )

    )

    content.append(

        Paragraph(
            f"Validation Status: {state.get('validation_status')}",
            styles["BodyText"]
        )

    )

    content.append(
        Spacer(
            1,
            10
        )
    )

    content.append(

        Paragraph(
            "Violations",
            styles["Heading2"]
        )

    )

    for violation in state.get(
        "violations",
        []
    ):

        content.append(

            Paragraph(
                f"• {violation}",
                styles["BodyText"]
            )

        )

    doc.build(
        content
    )

    return output_file