from datetime import datetime
import groupdocs.metadata as gm
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # SetMetadataProperties : How to set specific metadata properties using different criteria.\n")
            
    with gm.Metadata(constants.input_vsdx) as metadata:
        specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.time.created).either(gm.search.ContainsTagSpecification(gm.tagging.Tags.time.modified))
        now = datetime.now()
        property_value = gm.common.PropertyValue(now)
        affected = metadata.set_properties(specification, property_value)
        print(f"Properties set: {affected}")
        metadata.save(constants.output_vsdx)
