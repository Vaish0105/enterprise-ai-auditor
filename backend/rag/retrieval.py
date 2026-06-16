"""
=====================================================
Policy Retriever
Purpose : Retrieve policies from Qdrant
=====================================================
"""

from qdrant_client import (
    QdrantClient
)

from backend.rag.embedder import (
    get_embedding_model
)

from backend.config.settings import (
    settings
)


def retrieve_policies(
        query: str,
        limit: int = 5
):

    embeddings = (
        get_embedding_model()
    )

    query_vector = (
        embeddings.embed_query(
            query
        )
    )

    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )

    results = client.query_points(

        collection_name=
        "audit_policies",

        query=
        query_vector,

        limit=
        limit

    ).points

    retrieved = []

    for item in results:

        retrieved.append(
            item.payload
        )

    return retrieved