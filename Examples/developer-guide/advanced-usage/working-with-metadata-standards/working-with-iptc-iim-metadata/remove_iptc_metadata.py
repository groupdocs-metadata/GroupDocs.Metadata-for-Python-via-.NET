from groupdocs.metadata import Metadata


def remove_iptc_metadata():
    with Metadata("iptc.jpg") as metadata:
        root = metadata.get_root_package()
        # Assigning None drops the entire IPTC package
        root.iptc_package = None
        metadata.save("output.jpg")


if __name__ == "__main__":
    remove_iptc_metadata()