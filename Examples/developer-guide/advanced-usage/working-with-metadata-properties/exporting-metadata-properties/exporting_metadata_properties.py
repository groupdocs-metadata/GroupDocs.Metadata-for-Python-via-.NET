from groupdocs.metadata import Metadata
from groupdocs.metadata.export import ExportManager, ExportFormat


def exporting_metadata_properties():
    with Metadata("input.pdf") as metadata:
        # Collect the whole metadata tree as a list of properties
        properties = list(metadata.find_properties(lambda p: True))

        # Export them to an Excel workbook
        ExportManager(properties).export("export.xlsx", ExportFormat.XLSX)
        print(f"Exported {len(properties)} properties to export.xlsx")


if __name__ == "__main__":
    exporting_metadata_properties()