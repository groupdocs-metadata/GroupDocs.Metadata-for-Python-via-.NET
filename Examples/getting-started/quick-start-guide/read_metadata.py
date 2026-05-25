import os

from groupdocs.metadata import License, Metadata


def read_metadata():
    # Apply a license if one is present next to the script
    license_path = os.path.abspath("./GroupDocs.Metadata.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    with Metadata("./input.docx") as metadata:
        # `lambda p: True` matches every property in the file
        for prop in metadata.find_properties(lambda p: True):
            print(f"{prop.name} = {prop.value}")


if __name__ == "__main__":
    read_metadata()