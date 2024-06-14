import groupdocs.metadata as gm
import constants

def run():

    with gm.Metadata(constants.input_docx) as metadata:
        specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.person.creator).either(gm.search.ContainsTagSpecification(gm.tagging.Tags.person.editor)).either(gm.search.OfTypeSpecification(gm.common.MetadataPropertyType.STRING).both(gm.search.WithValueSpecification("John")))
        affected = metadata.remove_properties(specification)
        print(f"Properties removed: {affected}")
        metadata.save(constants.output_docx)
