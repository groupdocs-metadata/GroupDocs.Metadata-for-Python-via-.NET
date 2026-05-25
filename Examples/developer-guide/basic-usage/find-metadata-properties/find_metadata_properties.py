from groupdocs.metadata import Metadata
from groupdocs.metadata.tagging import Tags


def find_metadata_properties():
    # Fetch all the properties satisfying the predicate:
    # the property carries the "last editor" tag OR the "modified date/time" tag
    with Metadata("input.pptx") as metadata:
        properties = metadata.find_properties(
            lambda p: Tags.person.editor in list(p.tags)
            or Tags.time.modified in list(p.tags)
        )
        for prop in properties:
            print(f"Property name: {prop.name}, Property value: {prop.value}")


if __name__ == "__main__":
    find_metadata_properties()