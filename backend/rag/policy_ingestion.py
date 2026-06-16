"""
=====================================================
Policy Ingestion
=====================================================
"""

import uuid

from qdrant_client import (
    QdrantClient
)

from qdrant_client.models import (
    PointStruct
)

from backend.rag.policy_loader import (
    load_policies
)

from backend.rag.chunker import (
    create_chunks
)

from backend.rag.embedder import (
    get_embedding_model
)

from backend.config.settings import (
    settings
)


def ingest_policies():

    documents = load_policies()

    chunks = create_chunks(
        documents
    )

    embeddings = (
        get_embedding_model()
    )

    client = QdrantClient(

        url=
        settings.QDRANT_URL,

        api_key=
        settings.QDRANT_API_KEY
    )

    points = []

    for chunk in chunks:

        vector = embeddings.embed_query(

            chunk[
                "content"
            ]
        )

        points.append(

            PointStruct(

                id=str(
                    uuid.uuid4()
                ),

                vector=vector,

                payload={

                    "source":
                    chunk[
                        "source"
                    ],

                    "content":
                    chunk[
                        "content"
                    ]
                }
            )
        )

    client.upsert(

        collection_name=
        "audit_policies",

        points=points
    )

    print(
        f"Stored {len(points)} chunks"
    )