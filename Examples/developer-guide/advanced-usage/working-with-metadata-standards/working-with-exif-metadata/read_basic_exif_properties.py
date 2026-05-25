from groupdocs.metadata import Metadata


def read_basic_exif_properties():
    with Metadata("exif.tiff") as metadata:
        root = metadata.get_root_package()
        # The EXIF package is exposed on the root; it may be absent
        exif = getattr(root, "exif_package", None)
        if exif is not None:
            # Top-level EXIF tags
            print(exif.artist)
            print(exif.copyright)
            print(exif.image_description)
            print(exif.make)
            print(exif.model)
            print(exif.software)

            # The EXIF IFD sub-package holds camera/exposure details
            print(exif.exif_ifd_package.body_serial_number)
            print(exif.exif_ifd_package.camera_owner_name)
            print(exif.exif_ifd_package.user_comment)

            # The GPS sub-package holds geolocation tags
            print(exif.gps_package.altitude)
            print(exif.gps_package.latitude_ref)
            print(exif.gps_package.longitude_ref)


if __name__ == "__main__":
    read_basic_exif_properties()