
import os
import groupdocs.metadata as gm
import constants
import pathlib
from datetime import datetime

def run():
    files = os.listdir(constants.input_path)
    for file in files:
        with gm.Metadata(constants.input_path+file) as metadata:
            if metadata.file_format != gm.common.FileFormat.UNKNOWN and metadata.get_document_info().is_encrypted != True:
                print()
                print(file)

                specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.legal.copyright)
                affected = metadata.set_properties(specification, gm.common.PropertyValue("Copyright (C) 2011-2021 GroupDocs. All Rights Reserved."))
                print(f"Affected properties: {affected}")
                metadata.save(constants.output_path + "output" + pathlib.Path(file).suffix)
