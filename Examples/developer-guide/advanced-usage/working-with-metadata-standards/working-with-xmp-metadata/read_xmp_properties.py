from groupdocs.metadata import Metadata


def read_xmp_properties():
    with Metadata("xmp.png") as metadata:
        root = metadata.get_root_package()
        xmp = getattr(root, "xmp_package", None)
        if xmp is not None:
            # Standard schemes are reachable through xmp.schemes;
            # each may be absent, so guard before reading.
            if xmp.schemes.xmp_basic is not None:
                print(xmp.schemes.xmp_basic.creator_tool)
                print(xmp.schemes.xmp_basic.create_date)
                print(xmp.schemes.xmp_basic.modify_date)

            if xmp.schemes.dublin_core is not None:
                print(xmp.schemes.dublin_core.format)
                print(xmp.schemes.dublin_core.coverage)
                print(xmp.schemes.dublin_core.identifier)

            if xmp.schemes.photoshop is not None:
                print(xmp.schemes.photoshop.color_mode)
                print(xmp.schemes.photoshop.city)
                print(xmp.schemes.photoshop.date_created)


if __name__ == "__main__":
    read_xmp_properties()