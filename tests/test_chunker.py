from backend.rag.policy_loader import (
    load_policies
)

from backend.rag.chunker import (
    create_chunks
)

documents = load_policies()

chunks = create_chunks(
    documents
)

print("\nTOTAL CHUNKS\n")

print(
    len(chunks)
)

print("\nFIRST CHUNK\n")

print(
    chunks[0]
)