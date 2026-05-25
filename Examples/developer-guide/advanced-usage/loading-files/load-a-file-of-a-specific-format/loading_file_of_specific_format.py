from groupdocs.metadata import Metadata
from groupdocs.metadata.common import FileFormat
from groupdocs.metadata.options import LoadOptions


def loading_file_of_specific_format():
    load_options = LoadOptions(FileFormat.SPREADSHEET)

    with Metadata("input.xlsx", load_options) as metadata:
        root = metadata.get_root_package()
        # Use format-specific properties to extract or edit metadata
        print(f"Author: {root.document_properties.author}")


if __name__ == "__main__":
    loading_file_of_specific_format()