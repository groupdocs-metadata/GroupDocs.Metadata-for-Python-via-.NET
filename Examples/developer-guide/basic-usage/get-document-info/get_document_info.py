from groupdocs.metadata import Metadata


def get_document_info():
    # Open the file (the context manager releases it on exit)
    with Metadata("input.xlsx") as metadata:
        # Read basic information detected from the file's internal structure
        info = metadata.get_document_info()
        # Format, extension and MIME type come from the file_type descriptor
        print(f"File format: {info.file_type.file_format}")
        print(f"File extension: {info.file_type.extension}")
        print(f"MIME Type: {info.file_type.mime_type}")
        # Page/size/encryption details are exposed directly on the info object
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
        print(f"Is document encrypted: {info.is_encrypted}")


if __name__ == "__main__":
    get_document_info()