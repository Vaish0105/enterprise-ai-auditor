from backend.database.audit_history_repository import (
    get_all_audits
)

audits = get_all_audits()

for audit in audits:

    print(audit)