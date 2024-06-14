
import os
import groupdocs.metadata as gm
import constants
from datetime import datetime

def run():
    files = os.listdir(constants.input_path)
    for file in files:
        with gm.Metadata(constants.input_path+file) as metadata:
            if metadata.file_format != gm.common.FileFormat.UNKNOWN and metadata.get_document_info().is_encrypted != True:
                print()
                print(file)

                specification = gm.search.FallsIntoCategorySpecification(gm.tagging.Tags.content)
                properties = metadata.find_properties(specification)
                for property in properties:
                    print(f"Property name: {property.name}, Property value: {property.value}")
