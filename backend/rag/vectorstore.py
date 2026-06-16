"""
=====================================================
Qdrant Connection
=====================================================
"""

from qdrant_client import (
    QdrantClient
)

from backend.config.settings import (
    settings
)


def get_qdrant_client():

    client = QdrantClient(

        url=
        settings.QDRANT_URL,

        api_key=
        settings.QDRANT_API_KEY
    )

    return client