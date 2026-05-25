from groupdocs.metadata import Metadata
from groupdocs.metadata.formats.image import TiffTagID


def read_specific_exif_tag():
    with Metadata("exif.tiff") as metadata:
        root = metadata.get_root_package()
        exif = getattr(root, "exif_package", None)
        if exif is not None:
            # Index the package by TiffTagID to read one specific tag
            software = exif[TiffTagID.SOFTWARE]
            if software is not None:
                print(f"Software: {software.value}")

            # The same indexer works on the EXIF IFD sub-package
            comment = exif.exif_ifd_package[TiffTagID.USER_COMMENT]
            if comment is not None:
                print(f"Comment: {comment.interpreted_value}")


if __name__ == "__main__":
    read_specific_exif_tag()