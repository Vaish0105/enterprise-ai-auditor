"""
=====================================================
Qdrant Collection Setup
Purpose : Create Vector Collection
=====================================================
"""

from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    VectorParams,
    Distance
)

from backend.config.settings import (
    settings
)

def create_collection():

    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )

    collections = client.get_collections()

    collection_names = [
        c.name
        for c
        in collections.collections
    ]

    if "audit_policies" not in collection_names:

        client.create_collection(

            collection_name=
            "audit_policies",

            vectors_config=
            VectorParams(

                size=3072,

                distance=
                Distance.COSINE
            )
        )

        print(
            "Collection Created"
        )

    else:

        print(
            "Collection Already Exists"
        )