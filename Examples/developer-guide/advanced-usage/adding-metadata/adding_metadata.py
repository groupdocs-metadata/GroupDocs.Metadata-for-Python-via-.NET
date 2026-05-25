from datetime import datetime

from groupdocs.metadata import Metadata
from groupdocs.metadata.common import PropertyValue
from groupdocs.metadata.tagging import Tags


def adding_metadata():
    with Metadata("input.docx") as metadata:
        # Add the "last printed" date wherever it is a known but missing property
        property_value = PropertyValue(datetime.now())
        affected = metadata.add_properties(
            lambda p: Tags.time.printed in list(p.tags), property_value
        )
        print(f"Affected properties: {affected}")
        metadata.save("output.docx")


if __name__ == "__main__":
    adding_metadata()