from backend.config.settings import (
    settings
)

print(
    settings.QDRANT_URL
)

print(
    settings.OPENAI_API_KEY[:10]
)