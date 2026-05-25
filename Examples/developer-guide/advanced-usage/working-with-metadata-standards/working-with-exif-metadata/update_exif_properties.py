from groupdocs.metadata import Metadata
from groupdocs.metadata.standards.exif import ExifPackage


def update_exif_properties():
    with Metadata("input.jpg") as metadata:
        root = metadata.get_root_package()
        # Create an EXIF package if the image doesn't have one yet
        if getattr(root, "exif_package", None) is None:
            root.exif_package = ExifPackage()

        # Assign top-level EXIF properties
        root.exif_package.copyright = "Copyright (C) 2026 GroupDocs. All Rights Reserved."
        root.exif_package.image_description = "test image"
        root.exif_package.software = "GroupDocs.Metadata"

        # Assign properties on the EXIF IFD sub-package
        root.exif_package.exif_ifd_package.body_serial_number = "test"
        root.exif_package.exif_ifd_package.camera_owner_name = "GroupDocs"
        root.exif_package.exif_ifd_package.user_comment = "test comment"

        # Persist the changes
        metadata.save("output.jpg")


if __name__ == "__main__":
    update_exif_properties()