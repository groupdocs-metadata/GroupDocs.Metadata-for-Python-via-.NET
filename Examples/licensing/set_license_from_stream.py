import os

from groupdocs.metadata import License


def set_license_from_stream():
    license_path = os.path.abspath("./GroupDocs.Metadata.lic")
    if os.path.exists(license_path):
        # set_license also accepts a readable binary stream
        with open(license_path, "rb") as stream:
            License().set_license(stream)
        print("License set successfully.")
    else:
        print("License file not found; running in evaluation mode.")


if __name__ == "__main__":
    set_license_from_stream()