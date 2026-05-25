from groupdocs.metadata import Metadata


def load_from_local_disk():
    # Absolute or relative path to your document
    with Metadata("input.docx") as metadata:
        # Extract, edit or remove metadata here
        info = metadata.get_document_info()
        print(f"Loaded {info.file_type.file_format} ({info.size} bytes)")


if __name__ == "__main__":
    load_from_local_disk()