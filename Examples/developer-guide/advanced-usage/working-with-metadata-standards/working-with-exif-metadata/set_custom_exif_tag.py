from groupdocs.metadata import Metadata
from groupdocs.metadata.formats.image import TiffAsciiTag, TiffTagID
from groupdocs.metadata.standards.exif import ExifPackage


def set_custom_exif_tag():
    with Metadata("exif.tiff") as metadata:
        root = metadata.get_root_package()
        if getattr(root, "exif_package", None) is None:
            root.exif_package = ExifPackage()

        # Add known properties using typed TIFF tags
        root.exif_package.set(TiffAsciiTag(TiffTagID.ARTIST, "test artist"))
        root.exif_package.set(TiffAsciiTag(TiffTagID.SOFTWARE, "GroupDocs.Metadata"))

        metadata.save("output.tiff")


if __name__ == "__main__":
    set_custom_exif_tag()