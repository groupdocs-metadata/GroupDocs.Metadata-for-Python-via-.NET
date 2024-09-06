import groupdocs.metadata as gm
import groupdocs.metadata.formats.threed.stl as gmfts
from groupdocs.pycore import *
import constants


def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # StlReadNativeMetadataProperties : How to get metadata from a Stl file.\n")
            
    with gm.Metadata(constants.input_Stl) as metadata:
        root = cast(gmfts.StlRootPackage, metadata.get_root_package())
        for node in root.stl_package.nodes:
             print(f"Node name: {node.name}")