"""
=====================================================
Agent : Policy Agent
Purpose : Retrieve policies from Qdrant
=====================================================
"""

from backend.rag.retrieval import (
    retrieve_policies
)

from backend.rag.reranker import (
    rerank_results
)

def policy_agent(
        state
):

    document_type = state.get(
        "document_type",
        "unknown"
    )

    query = f"""
    Retrieve policy rules for
    {document_type}
    """

    policies = retrieve_policies(
    query=query,
    limit=10
)
    
    policies = rerank_results(
    query=query,
    documents=policies,
    top_k=3
)

    state[
        "policy_matches"
    ] = policies

    return state