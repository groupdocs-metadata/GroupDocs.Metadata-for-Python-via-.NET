
import os
import groupdocs.metadata as gm
import groupdocs.metadata as gm
import groupdocs.metadata.formats.document as gmfd
from groupdocs.pycore import *
import constants
import pathlib
from datetime import datetime

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Advanced Usage] # ImportMetadata : How to import metadata from json.\n")
    print("Before import:")      
    with gm.Metadata(constants.input_pdf) as metadata:
        root = cast(gmfd.PdfRootPackage, metadata.get_root_package())
        print(root.document_properties.author)
        print(root.document_properties.created_date)
        print(root.document_properties.producer)

        options = gm.importing.JsonImportOptions()
        manager = gm.importing.ImportManager(root)
        manager.import_metadata(constants.import_pdf, gm.importing.ImportFormat.JSON, options)
        metadata.save(constants.output_pdf)

    print("\nAfter import:")    
    with gm.Metadata(constants.output_pdf) as metadata:
        root = cast(gmfd.PdfRootPackage, metadata.get_root_package())
        print(root.document_properties.author)
        print(root.document_properties.created_date)
        print(root.document_properties.producer)