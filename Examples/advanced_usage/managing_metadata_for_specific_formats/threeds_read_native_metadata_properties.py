import groupdocs.metadata as gm
import groupdocs.metadata.formats.threed.threeds as gmftt
from groupdocs.pycore import *
import constants


def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # ThreeDSReadNativeMetadataProperties : How to get metadata from a ThreeDS file.\n")
     
    with gm.Metadata(constants.input_3ds) as metadata:
        root = cast(gmftt.ThreeDSRootPackage, metadata.get_root_package())
        for material in root.three_ds_package.materials:
             print(f"Material name: {material.name}")
        for node in root.three_ds_package.nodes:
             print(f"Node name: {node.name}")