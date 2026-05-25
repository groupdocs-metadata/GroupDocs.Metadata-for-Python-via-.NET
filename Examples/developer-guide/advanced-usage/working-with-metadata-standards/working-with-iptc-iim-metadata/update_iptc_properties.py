import uuid
from datetime import date, datetime

from groupdocs.metadata import Metadata
from groupdocs.metadata.standards.iptc import IptcApplicationRecord, IptcEnvelopeRecord, IptcRecordSet


def update_iptc_properties():
    with Metadata("input.jpg") as metadata:
        root = metadata.get_root_package()
        # Create the IPTC record set if the image has none
        if getattr(root, "iptc_package", None) is None:
            root.iptc_package = IptcRecordSet()

        # Fill the envelope record (create it first if missing)
        if root.iptc_package.envelope_record is None:
            root.iptc_package.envelope_record = IptcEnvelopeRecord()
        root.iptc_package.envelope_record.date_sent = datetime.now()
        root.iptc_package.envelope_record.product_id = str(uuid.uuid4())

        # Fill the application record (create it first if missing)
        if root.iptc_package.application_record is None:
            root.iptc_package.application_record = IptcApplicationRecord()
        root.iptc_package.application_record.by_line = "GroupDocs"
        root.iptc_package.application_record.headline = "test"
        root.iptc_package.application_record.by_line_title = "code sample"
        root.iptc_package.application_record.release_date = date.today()

        # Persist the changes
        metadata.save("output.jpg")


if __name__ == "__main__":
    update_iptc_properties()