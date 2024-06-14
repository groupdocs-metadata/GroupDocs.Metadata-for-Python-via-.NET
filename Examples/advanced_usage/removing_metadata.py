
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

                specification = gm.search.FallsIntoCategorySpecification(gm.tagging.Tags.content)
                affected = metadata.remove_properties(specification)
                print(f"Affected properties: {affected}")
                metadata.save(constants.output_path + "output" + pathlib.Path(file).suffix)
