"""
=====================================================
Module : PII Detector
Purpose : Detect sensitive information
=====================================================
"""

import re


# Detect PII
# Return findings
def detect_pii(
        text
):

    findings = []

    # Email detection
    # Identify email addresses
    emails = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if emails:

        findings.append(
            {
                "type": "email",
                "count": len(emails)
            }
        )

    # Phone detection
    # Identify phone numbers
    phones = re.findall(
        r"\d{10}",
        text
    )

    if phones:

        findings.append(
            {
                "type": "phone",
                "count": len(phones)
            }
        )

    return findings