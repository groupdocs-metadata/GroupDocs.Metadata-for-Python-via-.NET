from groupdocs.metadata import Metadata
from groupdocs.metadata.standards.iptc import (
    IptcApplicationRecordDataSet, IptcDataSet, IptcRecordSet, IptcRecordType,
)


def set_custom_iptc_dataset():
    with Metadata("iptc.psd") as metadata:
        root = metadata.get_root_package()
        if getattr(root, "iptc_package", None) is None:
            root.iptc_package = IptcRecordSet()

        # Add a known property using the DataSet API
        root.iptc_package.set(IptcDataSet(
            int(IptcRecordType.APPLICATION_RECORD),
            int(IptcApplicationRecordDataSet.BYLINE_TITLE),
            "test code sample",
        ))

        # Add a fully custom IPTC DataSet
        root.iptc_package.set(IptcDataSet(255, 255, bytes([1, 2, 3])))

        metadata.save("output.psd")


if __name__ == "__main__":
    set_custom_iptc_dataset()