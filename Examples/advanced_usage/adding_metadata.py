
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
                specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.time.printed)
                now = datetime.now()
                property_value = gm.common.PropertyValue(now)
                affected = metadata.add_properties(specification, property_value)
                print(f"Affected properties: {affected}");
                filename, file_extension = os.path.splitext(file)
                metadata.save(constants.output_path + "output" + file_extension)
