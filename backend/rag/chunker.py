"""
=====================================================
Chunker
Purpose : Split policies
=====================================================
"""

def split_text(text, chunk_size=800, chunk_overlap=100):
    if chunk_size <= chunk_overlap:
        raise ValueError("chunk_size must be larger than chunk_overlap")

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        if end >= text_length:
            break
        start = end - chunk_overlap

    return chunks


def create_chunks(documents):
    # Use the local split_text function instead of an undefined RecursiveCharacterTextSplitter
    chunks = []

    for doc in documents:
        split_docs = split_text(doc.get("content", ""), chunk_size=800, chunk_overlap=100)

        for chunk in split_docs:
            chunks.append({
                "source": doc.get("file_name"),
                "content": chunk,
            })

    return chunks