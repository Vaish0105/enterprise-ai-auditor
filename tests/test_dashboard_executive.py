from backend.database.dashboard_repository import (

    get_approved_audits,

    get_rejected_audits
)

print(

    "Approved:",
    get_approved_audits()

)

print(

    "Rejected:",
    get_rejected_audits()

)