from datetime import date

from groupdocs.metadata import Metadata
from groupdocs.metadata.standards.xmp.schemes import XmpBasicPackage, XmpCameraRawPackage, XmpDublinCorePackage


def update_xmp_properties():
    with Metadata("xmp.gif") as metadata:
        root = metadata.get_root_package()
        xmp = getattr(root, "xmp_package", None)
        if xmp is not None:
            if xmp.schemes.dublin_core is None:
                xmp.schemes.dublin_core = XmpDublinCorePackage()
            xmp.schemes.dublin_core.format = "image/gif"

            if xmp.schemes.camera_raw is None:
                xmp.schemes.camera_raw = XmpCameraRawPackage()
            xmp.schemes.camera_raw.shadows = 50
            xmp.schemes.camera_raw.camera_profile = "test"

            # Replace the whole scheme to drop old values
            xmp.schemes.xmp_basic = XmpBasicPackage()
            xmp.schemes.xmp_basic.create_date = date.today()
            xmp.schemes.xmp_basic.rating = 5

            metadata.save("output.gif")


if __name__ == "__main__":
    update_xmp_properties()