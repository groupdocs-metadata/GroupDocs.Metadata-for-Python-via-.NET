import groupdocs.metadata as gm
import constants

def run():

    with gm.Metadata(constants.input_pdf) as metadata:
        affected = metadata.sanitize()
        print(f"Properties removed: {affected}")
        metadata.save(constants.output_pdf)
