from groupdocs.metadata import Metadata


def remove_xmp_metadata():
    with Metadata("xmp.jpg") as metadata:
        root = metadata.get_root_package()
        # Assigning None drops the entire XMP packet
        root.xmp_package = None
        metadata.save("output.jpg")


if __name__ == "__main__":
    remove_xmp_metadata()