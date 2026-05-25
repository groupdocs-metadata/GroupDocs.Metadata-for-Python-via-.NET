from groupdocs.metadata import Metadata
from groupdocs.metadata.options import LoadOptions


def load_password_protected_document():
    # Specify the password
    load_options = LoadOptions()
    load_options.password = "123"

    with Metadata("protected.docx", load_options) as metadata:
        # Extract, edit or remove metadata here
        print(f"Opened protected {metadata.file_format} document")


if __name__ == "__main__":
    load_password_protected_document()