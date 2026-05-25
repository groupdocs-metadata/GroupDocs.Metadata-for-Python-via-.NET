from groupdocs.metadata import Metadata


def read_exif_tags():
    with Metadata("exif.jpg") as metadata:
        root = metadata.get_root_package()
        exif = getattr(root, "exif_package", None)
        if exif is not None:
            # to_list() yields every raw tag (id + value) at each level
            for tag in exif.to_list():
                print(f"{tag.tag_id} = {tag.value}")

            # ...including the EXIF IFD sub-package
            for tag in exif.exif_ifd_package.to_list():
                print(f"{tag.tag_id} = {tag.value}")

            # ...and the GPS sub-package
            for tag in exif.gps_package.to_list():
                print(f"{tag.tag_id} = {tag.value}")


if __name__ == "__main__":
    read_exif_tags()