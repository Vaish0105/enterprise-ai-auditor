"""
=====================================================
BGE Re-ranker
Purpose : Improve retrieval accuracy
=====================================================
"""

from FlagEmbedding import (
    FlagReranker
)


# Load reranker model
# Executed once
reranker = FlagReranker(

    "BAAI/bge-reranker-large",

    use_fp16=False
)


# Re-rank retrieved chunks
# Return best chunks
def rerank_results(

        query,

        documents,

        top_k=3
):

    # Store scores
    # Query-document pairs
    scored_results = []

    # Score every document
    # Relevance calculation
    for doc in documents:

        score = reranker.compute_score(

            [

                query,

                doc[
                    "content"
                ]
            ]
        )

        scored_results.append(

            (
                score,
                doc
            )
        )

    # Highest score first
    # Most relevant first
    scored_results.sort(

        reverse=True,

        key=lambda x: x[0]
    )

    # Return best documents
    # Top K results
    return [

        item[1]

        for item

        in scored_results[
            :top_k
        ]
    ]