from backend.database.dashboard_repository import *

print(
    "Total Audits:",
    get_total_audits()
)

print(
    "Average Risk:",
    get_average_risk()
)

print(
    "Failed Validations:",
    get_failed_validations()
)

print(
    "Policies:",
    get_total_policies()
)