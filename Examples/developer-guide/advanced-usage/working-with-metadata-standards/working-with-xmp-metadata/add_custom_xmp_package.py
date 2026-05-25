from datetime import date

from groupdocs.metadata import Metadata
from groupdocs.metadata.standards.xmp import XmpArray, XmpArrayType, XmpPackage, XmpPacketWrapper


def add_custom_xmp_package():
    with Metadata("input.jpg") as metadata:
        root = metadata.get_root_package()
        packet = XmpPacketWrapper()

        custom = XmpPackage("gd", "https://groupdocs.com")
        custom.set("gd:Copyright", "Copyright (C) 2026 GroupDocs. All Rights Reserved.")
        custom.set("gd:CreationDate", date.today())
        custom.set("gd:Company", XmpArray.from_(["Aspose", "GroupDocs"], XmpArrayType.ORDERED))
        packet.add_package(custom)

        root.xmp_package = packet
        metadata.save("output.jpg")


if __name__ == "__main__":
    add_custom_xmp_package()