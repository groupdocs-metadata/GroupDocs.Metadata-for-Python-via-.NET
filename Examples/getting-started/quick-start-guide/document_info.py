from groupdocs.metadata import Metadata


def document_info():
    with Metadata("./input.docx") as metadata:
        # get_document_info() reads basic facts without walking the metadata tree
        info = metadata.get_document_info()
        print(f"Format: {info.file_type.file_format}")
        print(f"MIME type: {info.file_type.mime_type}")
        print(f"Pages: {info.page_count}")
        print(f"Size: {info.size} bytes")
        print(f"Encrypted: {info.is_encrypted}")


if __name__ == "__main__":
    document_info()