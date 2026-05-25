from datetime import datetime

from groupdocs.metadata import Metadata
from groupdocs.metadata.common import PropertyValue
from groupdocs.metadata.tagging import Tags


def set_metadata_properties():
    with Metadata("input.vsdx") as metadata:
        # The value to write into every matching property
        property_value = PropertyValue(datetime.now())
        # set_properties = add-or-update: the predicate selects the
        # "created" and "modified" date/time properties across all packages
        affected = metadata.set_properties(
            lambda p: Tags.time.created in list(p.tags)
            or Tags.time.modified in list(p.tags),
            property_value,
        )
        print(f"Properties set: {affected}")
        # Persist the changes to a new file
        metadata.save("output.vsdx")


if __name__ == "__main__":
    set_metadata_properties()