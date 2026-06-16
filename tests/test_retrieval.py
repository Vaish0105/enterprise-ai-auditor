from backend.rag.retrieval import (
    retrieve_policies
)

results = retrieve_policies(

    "hotel reimbursement policy"
)

print("\nRETRIEVED\n")

for item in results:

    print(item)