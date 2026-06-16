"""
=====================================================
Policy Loader
Purpose : Load policy documents
=====================================================
"""

from pathlib import Path


def load_policies():

    documents = []

    policy_path = Path(
        "data/policies"
    )

    for file in policy_path.glob(
        "*.txt"
    ):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            documents.append(

                {
                    "file_name":
                    file.name,

                    "content":
                    f.read()
                }
            )

    return documents