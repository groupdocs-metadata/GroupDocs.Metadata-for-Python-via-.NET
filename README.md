# GroupDocs.Metadata-for-Python-via-.NET
GroupDocs.Metadata for Python provides easy ways to [Manage Document Metadata via Python](https://products.groupdocs.com/metadata/python-net/). It enables you to read, write, update and remove metadata of a [wide range of file formats](https://docs.groupdocs.com/metadata/python-net/supported-document-formats/) including documents, images, emails, archives and many more. It also provides the feature to search and update metadata in document files.


## Read, Write, Update & Remove Document Metadata

- Read, update and remove metadata from 60+ popular file formats.
- Search, update and remove particular metadata properties that satisfy a specification.
- Use tags to easily manipulate most common metadata properties in a unified manner.
- [Load & work with password-protected documents](https://docs.groupdocs.com/metadata/python-net/load-a-password-protected-document/).
- Extract information about hidden document pages, digital signatures, user comments, revisions and more.
- Supports most popular metadata standards: IPTC, XMP, EXIF, Image Resources.
- Manipulate native metadata properties in various formats, extracting technical information from images, audio and video files.
- [Calculate common document statistics](https://docs.groupdocs.com/metadata/python-net/get-document-info/).
- Auto-detect the format and MIME type of a file by its internal structure.
- Supports various audio tags including ID3, Lyrics & APE.

## Getting Started with GroupDocs.Metadata for Node.js via Java
### Installation

Fetch the package and install GroupDocs.Metadata. Run this command: pip install groupdocs.metadata

If you already have GroupDocs.Metadata installed and want to get the latest version, you have to run: pip install --upgrade groupdocs.metadata instead.


## Get Document Info

```python
// constants.input_xlsx is an absolute or relative path to your document. Ex: @"C:\Docs\source.xlsx"
with gm.Metadata(constants.input_xlsx) as metadata:
        info = metadata.get_document_info()
        print(f"File format: {info.file_type.file_format}")
        print(f"File extension: {info.file_type.extension}")
        print(f"MIME Type: {info.file_type.mime_type}")
        print(f"Number of pages: {info.page_count}")
        print(f"Document size: {info.size} bytes")
        print(f"Is document encrypted: {info.is_encrypted}")
```

## Add or Update Metadata Properties Satisfying a Predicate

```python
// constants.input_vsdx is an absolute or relative path to your document. Ex: @"C:\Docs\source.vsdx"
with gm.Metadata(constants.input_vsdx) as metadata:
        specification = gm.search.ContainsTagSpecification(gm.tagging.Tags.time.created).either(gm.search.ContainsTagSpecification(gm.tagging.Tags.time.modified))
        now = datetime.now()
        property_value = gm.common.PropertyValue(now)
        affected = metadata.set_properties(specification, property_value)
        print(f"Properties set: {affected}")
        metadata.save(constants.output_vsdx)
}
```

[Home](https://www.groupdocs.com/) | [Product Page](https://products.groupdocs.com/metadata/python-net) | [Documentation](https://docs.groupdocs.com/metadata/python-net/) | [Demos](https://products.groupdocs.app/metadata/family) | [API Reference](https://apireference.groupdocs.com/python-net/metadata) | [Examples](https://github.com/groupdocs-metadata/GroupDocs.metadata-for-Python-via-.NET/tree/master/Examples) | [Blog](https://blog.groupdocs.com/category/metadata/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/metadata) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
