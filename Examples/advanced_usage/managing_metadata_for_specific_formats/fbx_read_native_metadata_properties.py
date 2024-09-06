import groupdocs.metadata as gm
import groupdocs.metadata.formats.threed.fbx as gmftf
from groupdocs.pycore import *
import constants


def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # FbxReadNativeMetadataProperties : How to get metadata from a Fbx file.\n")
    with gm.Metadata(constants.input_Fbx) as metadata:
        root = cast(gmftf.FbxRootPackage, metadata.get_root_package())
        print(root.fbx_package.author);
        print(root.fbx_package.comment);
        print(root.fbx_package.application_name);
        print(root.fbx_package.application_vendor);
        print(root.fbx_package.name);
        print(root.fbx_package.application_version);
        print(root.fbx_package.url);
        for node in root.fbx_package.nodes:
             print(f"Node name: {node.name}")