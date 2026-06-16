from backend.rag.embedder import (
    get_embedding_model
)

embeddings = (
    get_embedding_model()
)

vector = embeddings.embed_query(

    "Hotel reimbursement limit is ₹5000"
)

print(
    len(vector)
)

print(
    vector[:5]
)