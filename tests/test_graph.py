from backend.graph.audit_graph import (
    audit_graph
)

result = audit_graph.invoke(
    {
        "file_path":
        "test_files/hotel_invoice.jpg"
    }
)

print("\nFINAL STATE\n")

print(result)

print("\nAUDIT REPORT\n")

print(
    result.get(
        "audit_report"
    )
)