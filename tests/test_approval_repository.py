from backend.database.approval_repository import (
    get_pending_approvals
)

results = get_pending_approvals()

for row in results:

    print(row)