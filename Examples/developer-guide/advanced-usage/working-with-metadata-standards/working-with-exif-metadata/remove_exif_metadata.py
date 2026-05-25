from groupdocs.metadata import Metadata


def remove_exif_metadata():
    with Metadata("exif.jpg") as metadata:
        root = metadata.get_root_package()
        # Assigning None drops the entire EXIF package
        root.exif_package = None
        metadata.save("output.jpg")


if __name__ == "__main__":
    remove_exif_metadata()