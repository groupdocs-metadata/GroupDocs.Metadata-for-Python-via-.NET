from groupdocs.metadata import Metadata


def read_basic_iptc_properties():
    with Metadata("iptc.jpg") as metadata:
        root = metadata.get_root_package()
        iptc = getattr(root, "iptc_package", None)
        if iptc is not None:
            # The envelope record carries transmission-level fields
            if iptc.envelope_record is not None:
                print(iptc.envelope_record.date_sent)
                print(iptc.envelope_record.destination)
                print(iptc.envelope_record.file_format)

            # The application record carries the editorial fields
            if iptc.application_record is not None:
                print(iptc.application_record.headline)
                print(iptc.application_record.by_line)
                print(iptc.application_record.caption_abstract)
                print(iptc.application_record.city)
                print(iptc.application_record.date_created)


if __name__ == "__main__":
    read_basic_iptc_properties()