from groupdocs.metadata import Metadata
from groupdocs.metadata.tagging import Tags


def extracting_metadata():
    with Metadata("input.docx") as metadata:
        # Find every property whose tags fall into the "content" category
        properties = metadata.find_properties(
            lambda p: any(tag.category == Tags.content for tag in p.tags)
        )
        for prop in properties:
            print(f"Property name: {prop.name}, Property value: {prop.value}")


if __name__ == "__main__":
    extracting_metadata()