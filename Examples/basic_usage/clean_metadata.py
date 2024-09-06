import groupdocs.metadata as gm
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # CleanMetadata : How to remove all detected metadata packages/properties from a file.\n")
            
    with gm.Metadata(constants.input_pdf) as metadata:
        affected = metadata.sanitize()
        print(f"Properties removed: {affected}")
        metadata.save(constants.output_pdf)
