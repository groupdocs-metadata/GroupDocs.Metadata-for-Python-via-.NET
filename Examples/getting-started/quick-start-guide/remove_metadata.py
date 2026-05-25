import os

from groupdocs.metadata import License, Metadata


def remove_metadata():
    license_path = os.path.abspath("./GroupDocs.Metadata.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    with Metadata("./input.docx") as metadata:
        # sanitize() strips every detected property; save() needs a license
        removed = metadata.sanitize()
        print(f"Removed {removed} properties")
        metadata.save("./clean.docx")


if __name__ == "__main__":
    remove_metadata()