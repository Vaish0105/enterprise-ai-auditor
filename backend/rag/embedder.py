"""
=====================================================
Embedding Model
=====================================================
"""

from langchain_openai import (
    OpenAIEmbeddings
)

from backend.config.settings import (
    settings
)


def get_embedding_model():

    return OpenAIEmbeddings(

        model=
        "text-embedding-3-large",

        api_key=
        settings.OPENAI_API_KEY
    )