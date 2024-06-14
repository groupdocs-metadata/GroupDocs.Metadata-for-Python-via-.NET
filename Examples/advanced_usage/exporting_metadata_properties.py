
import os
import groupdocs.metadata as gm
import constants
from datetime import datetime

def run():
    with gm.Metadata(constants.input_doc) as metadata:
        root = metadata.get_root_package()
        manager = gm.export.ExportManager(root)
        manager.export(constants.output_xls, gm.export.ExportFormat.XLS);
