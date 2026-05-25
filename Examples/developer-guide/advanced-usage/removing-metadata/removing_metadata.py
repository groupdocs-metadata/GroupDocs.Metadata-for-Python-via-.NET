from groupdocs.metadata import Metadata
from groupdocs.metadata.tagging import Tags


def removing_metadata():
    with Metadata("input.docx") as metadata:
        # Remove every property whose tags fall into the "content" category
        affected = metadata.remove_properties(
            lambda p: any(tag.category == Tags.content for tag in p.tags)
        )
        print(f"Affected properties: {affected}")
        metadata.save("output.docx")


if __name__ == "__main__":
    removing_metadata()