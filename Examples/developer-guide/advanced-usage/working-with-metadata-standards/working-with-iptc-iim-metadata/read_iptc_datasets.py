from groupdocs.metadata import Metadata


def read_iptc_datasets():
    with Metadata("iptc.psd") as metadata:
        root = metadata.get_root_package()
        iptc = getattr(root, "iptc_package", None)
        if iptc is not None:
            # to_data_set_list() returns every raw IPTC dataset
            for dataset in iptc.to_data_set_list():
                print(dataset.record_number)       # record (e.g. 1=envelope, 2=application)
                print(dataset.data_set_number)     # dataset id within the record
                print(dataset.alternative_name)    # human-readable name
                print(dataset.value.raw_value)     # underlying value


if __name__ == "__main__":
    read_iptc_datasets()