import groupdocs.metadata as gm
import constants

def run():

    with gm.Metadata(constants.input_pptx) as metadata:
        specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.person.editor).either(gm.search.ContainsTagSpecification(gm.tagging.Tags.time.modified))
        properties = metadata.find_properties(specification)
        for property in properties:
             print(f"Property name: {property.name}, Property value: {property.value}")