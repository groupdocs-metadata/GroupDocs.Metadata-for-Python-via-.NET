import os

from groupdocs.metadata import License


def set_license_from_file():
    # Resolve the license path relative to the current working directory
    license_path = os.path.abspath("./GroupDocs.Metadata.lic")
    if os.path.exists(license_path):
        # Apply the license once, before using any other Metadata API
        license = License()
        license.set_license(license_path)
        print("License set successfully.")
    else:
        print("License file not found; running in evaluation mode.")


if __name__ == "__main__":
    set_license_from_file()