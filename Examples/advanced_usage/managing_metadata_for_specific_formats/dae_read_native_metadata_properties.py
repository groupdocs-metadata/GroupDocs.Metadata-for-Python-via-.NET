import groupdocs.metadata as gm
import groupdocs.metadata.formats.threed.dae as gmftd
from groupdocs.pycore import *
import constants


def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # DaeReadNativeMetadataProperties : How to get metadata from a Dae file.\n")
            
    with gm.Metadata(constants.input_Dae) as metadata:
        root = cast(gmftd.DaeRootPackage, metadata.get_root_package())
        print(root.dae_package.author);
        print(root.dae_package.comment);
        print(root.dae_package.creation_time);
        print(root.dae_package.modification_time);
        print(root.dae_package.name);
        print(root.dae_package.title);
        for node in root.dae_package.nodes:
             print(f"Node name: {node.name}")