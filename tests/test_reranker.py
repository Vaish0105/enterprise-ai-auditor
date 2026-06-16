from backend.rag.retrieval import (
    retrieve_policies
)

from backend.rag.reranker import (
    rerank_results
)

query = (
    "hotel reimbursement policy"
)

retrieved = retrieve_policies(

    query,

    limit=10
)

results = rerank_results(

    query,

    retrieved,

    top_k=3
)

print("\nRERANKED RESULTS\n")

for item in results:

    print(item)