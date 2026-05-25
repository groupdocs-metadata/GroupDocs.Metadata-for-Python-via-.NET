from groupdocs.metadata import Metadata
from groupdocs.metadata.common import MetadataPropertyType
from groupdocs.metadata.tagging import Tags


def remove_metadata_properties():
    # Remove all the properties satisfying the predicate:
    #   the property carries the "author" tag, OR
    #   the property carries the "last editor" tag, OR
    #   the property is a string whose value equals "John"
    #   (to wipe any mention of John from the detected metadata)
    with Metadata("input.docx") as metadata:
        affected = metadata.remove_properties(
            lambda p: Tags.person.creator in list(p.tags)
            or Tags.person.editor in list(p.tags)
            or (p.value.type == MetadataPropertyType.STRING and str(p.value) == "John")
        )
        print(f"Properties removed: {affected}")
        metadata.save("output.docx")


if __name__ == "__main__":
    remove_metadata_properties()