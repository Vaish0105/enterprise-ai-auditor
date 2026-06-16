from backend.database.search_repository import (
    search_audits
)

results = search_audits(

    "hotel_invoice",

    "pending",

    80
)

for row in results:

    print(row)