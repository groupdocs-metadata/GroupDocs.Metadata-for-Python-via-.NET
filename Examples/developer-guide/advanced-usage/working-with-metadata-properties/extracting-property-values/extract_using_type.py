from groupdocs.metadata import Metadata
from groupdocs.metadata.common import MetadataPropertyType


def extract_using_type():
    with Metadata("input.docx") as metadata:
        # Fetch all metadata properties from the file
        properties = metadata.find_properties(lambda p: True)
        for prop in properties:
            # Process string and date/time properties only (as an example)
            if prop.value.type == MetadataPropertyType.STRING:
                print(f"{prop.name} (string): {prop.value.raw_value}")
            elif prop.value.type == MetadataPropertyType.DATE_TIME:
                print(f"{prop.name} (datetime): {prop.value.raw_value}")


if __name__ == "__main__":
    extract_using_type()