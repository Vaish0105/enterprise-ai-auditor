from backend.database.audit_details_repository import (
    get_audit_details
)

result = get_audit_details(10)

print(result)