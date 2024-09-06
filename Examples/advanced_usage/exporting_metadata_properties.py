
import os
import groupdocs.metadata as gm
import constants
from datetime import datetime

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # ExportingMetadataProperties : How to export metadata properties to an Excel workbook.\n")
            
    with gm.Metadata(constants.input_doc) as metadata:
        root = metadata.get_root_package()
        manager = gm.export.ExportManager(root)
        manager.export(constants.output_xls, gm.export.ExportFormat.XLS);
