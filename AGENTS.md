<!-- generator:skip -->
# GroupDocs.Metadata for Python via .NET -- AGENTS.md

> Instructions for AI agents working with this package.

Read, edit, and remove metadata from documents, spreadsheets, presentations, PDFs, images, audio, and video -- 110+ formats, with support for XMP, EXIF, IPTC, Image Resource Blocks, and ID3.

## Install

```bash
pip install groupdocs-metadata-net
```

**Python**: 3.5 - 3.14 | **Platforms**: Windows, Linux, macOS

## Resources

| Resource | URL |
|---|---|
| Documentation | https://docs.groupdocs.com/metadata/python-net/ |
| LLM-optimized docs | https://docs.groupdocs.com/metadata/python-net/llms-full.txt |
| API reference | https://reference.groupdocs.com/metadata/python-net/ |
| Code examples | https://docs.groupdocs.com/metadata/python-net/developer-guide/ |
| Release notes | https://releases.groupdocs.com/metadata/python-net/release-notes/ |
| PyPI | https://pypi.org/project/groupdocs-metadata-net/ |
| Free support forum | https://forum.groupdocs.com/c/metadata/ |
| Temporary license | https://purchase.groupdocs.com/temporary-license |

## MCP Server

If your environment has MCP configured, you can connect your AI tool to the GroupDocs documentation server for on-demand API lookups:

```json
{
  "mcpServers": {
    "groupdocs-docs": {
      "url": "https://docs.groupdocs.com/mcp"
    }
  }
}
```

Works with Claude Code (`~/.claude/settings.json`), Cursor (`.cursor/mcp.json`), VS Code Copilot (`.vscode/mcp.json`), and any MCP-compatible client. If MCP is unavailable, fall back to the LLM-optimized docs URL above and this file -- both are shipped inside the wheel.

## Imports

```python
from groupdocs.metadata import License, Metadata, Metered
from groupdocs.metadata.common import (
    FileFormat, FileType, MetadataPackage, RootMetadataPackage, CustomPackage,
    MetadataProperty, PropertyValue, PropertyDescriptor,
    MetadataPropertyType, MetadataType, PropertyAccessLevels, ByteOrder,
)
from groupdocs.metadata.tagging import Tags  # plus the *TagCategory classes
from groupdocs.metadata.options import LoadOptions, PreviewOptions, PreviewFormats
from groupdocs.metadata.export import ExportManager, ExportFormat, CsvExportOptions, ExcelExportOptions, JsonExportOptions, XmlExportOptions
from groupdocs.metadata.import_ import ImportManager, ImportFormat, ImportOptions, JsonImportOptions
from groupdocs.metadata.logging import ConsoleLogger, FileLogger, Logging
from groupdocs.metadata.exceptions import (
    GroupDocsMetadataException, DocumentProtectedException,
    InvalidFormatException, MetadataValidationException, XmpException,
)
# Format-specific packages live under groupdocs.metadata.standards.* and groupdocs.metadata.formats.*
```

## Read metadata

```python
from groupdocs.metadata import Metadata

with Metadata("document.docx") as metadata:
    root = metadata.get_root_package()
    print("Format:", root.file_type.file_format)
    for prop in metadata.find_properties(lambda p: True):
        print(f"{prop.name} = {prop.value}")
```

## Get document info

```python
with Metadata("input.xlsx") as metadata:
    info = metadata.get_document_info()
    print(info.file_type.file_format, info.file_type.mime_type)
    print("pages:", info.page_count, "size:", info.size, "encrypted:", info.is_encrypted)
```

## Searching properties (predicates, NOT a `search` namespace)

This wrapper has **no `Specification` / `search` namespace** (unlike the .NET API). You filter with **Python callables** passed to `find_properties` / `set_properties` / `remove_properties` / `add_properties` / `update_properties`. The callable receives one `MetadataProperty` and returns `bool`.

```python
from groupdocs.metadata.tagging import Tags
from groupdocs.metadata.common import MetadataPropertyType

# by tag membership
metadata.find_properties(lambda p: Tags.person.creator in list(p.tags))
# combine tags (OR)
metadata.find_properties(lambda p: Tags.time.created in list(p.tags) or Tags.time.modified in list(p.tags))
# by tag category
metadata.find_properties(lambda p: any(t.category == Tags.content for t in p.tags))
# by name / value type / interpreted value
metadata.find_properties(lambda p: p.name == "Author")
metadata.find_properties(lambda p: p.value.type == MetadataPropertyType.STRING)
metadata.find_properties(lambda p: p.interpreted_value is not None)
# everything
metadata.find_properties(lambda p: True)
```

**`find_properties` returns a .NET collection object** (supports `for`/`len()`), not a Python `list`. Wrap it with `list(...)` when an API needs a real list (e.g. `ExportManager`).

## Set / update / remove / sanitize, then save

```python
from datetime import datetime
from groupdocs.metadata import Metadata
from groupdocs.metadata.common import PropertyValue
from groupdocs.metadata.tagging import Tags

with Metadata("input.docx") as metadata:
    # set = add-or-update properties matching the predicate
    metadata.set_properties(lambda p: Tags.time.created in list(p.tags), PropertyValue(datetime.now()))
    metadata.remove_properties(lambda p: Tags.person.creator in list(p.tags))
    metadata.save("output.docx")

# strip everything in one call
with Metadata("input.pdf") as metadata:
    removed = metadata.sanitize()
    metadata.save("clean.pdf")
```

## Export the metadata tree

`ExportManager` takes a **list of properties** (its only constructor is `ExportManager(Iterable[MetadataProperty])`). Pass `list(...)` — a package object is not accepted directly.

```python
from groupdocs.metadata.export import ExportManager, ExportFormat

with Metadata("input.pdf") as metadata:
    properties = list(metadata.find_properties(lambda p: True))
    ExportManager(properties).export("metadata.xlsx", ExportFormat.XLSX)
    # ExportFormat: XLS, XLSX, XML, CSV, JSON
```

## Format-specific standards (EXIF / XMP / IPTC)

Access via the root package; assign `None` to remove a package.

```python
with Metadata("photo.jpg") as metadata:
    root = metadata.get_root_package()
    exif = getattr(root, "exif_package", None)
    if exif is not None:
        print(exif.make, exif.model)
        exif.copyright = "(C) 2026 Example"
    # root.xmp_package / root.iptc_package work the same way
    metadata.save("photo_out.jpg")
```

## Licensing

```python
from groupdocs.metadata import License

# From file
License().set_license("path/to/license.lic")

# From stream
with open("license.lic", "rb") as f:
    License().set_license(f)
```

Or auto-apply: `export GROUPDOCS_LIC_PATH="path/to/license.lic"`

**Evaluation vs licensed.** Without a license the library runs but (1) reads only the first few properties of each metadata package and (2) **`save()` is disabled** — it raises `GroupDocsMetadataException: "Could not save the file. Evaluation only."`. Apply a license (or set `GROUPDOCS_LIC_PATH`) to lift both. A 30-day full license is free: https://purchase.groupdocs.com/temporary-license

## API Reference

### Metadata

| Method | Returns | Description |
|---|---|---|
| `Metadata(file_path / stream / uri[, load_options])` | | Open a file by path, binary stream, or URI; optional `LoadOptions`. Use as a context manager. |
| `get_root_package()` | `RootMetadataPackage` | Root of the metadata tree; exposes format-specific packages (`document_properties`, `exif_package`, `xmp_package`, `iptc_package`, …) and `file_type`. |
| `get_document_info()` | `IDocumentInfo` | `file_type` (→ `file_format`, `extension`, `mime_type`), `page_count`, `size`, `is_encrypted`, `pages`. |
| `find_properties(predicate)` | collection | Properties matching a `lambda p: bool` (wrap in `list()` for a Python list). |
| `set_properties(predicate, value)` | `int` | Add-or-update matching properties; returns affected count. |
| `update_properties(predicate, value)` | `int` | Update existing matching properties. |
| `add_properties(predicate, value)` | `int` | Add known-but-missing matching properties to existing packages. |
| `remove_properties(predicate)` | `int` | Remove matching properties; returns removed count. |
| `sanitize()` | `int` | Remove every detected property; returns removed count. |
| `save([file_path / stream])` | `None` | Save to a new path/stream, or in place when called with no argument. |
| `generate_preview(preview_options)` | `None` | Render page previews (see `groupdocs.metadata.options.PreviewOptions`). |
| `copy_to(metadata_package)` | `None` | Copy properties into another package. |
| `file_format` | `FileFormat` | Detected format enum (property). |

### License / Metered

`License().set_license(path_or_stream)` · `Metered().set_metered_key(public, private)` · `Metered.get_consumption_quantity()` · `Metered.get_consumption_credit()`

## Key Patterns

- **Properties**: use `snake_case` -- auto-mapped to .NET `PascalCase`
- **Context managers**: `with Metadata(...) as md:` ensures the file handle is released
- **Predicates**: pass `lambda p: <bool>` to `find_/set_/add_/remove_/update_properties` (there is no `Specification` API)
- **Collections**: `for x in result` and `len(result)` work; call `list(result)` to get a Python list
- **Streams**: pass `open("file", "rb")` or `io.BytesIO(data)` where a path is expected; `BytesIO` is updated after `save(stream)`
- **Enums**: case-insensitive, lazy-loaded (e.g., `FileType.DOCX`, `ExportFormat.JSON`)
- **Format packages**: read/write via `root.exif_package` / `.xmp_package` / `.iptc_package`; set to `None` to remove

## Platform Requirements

| Platform | Requirements |
|---|---|
| Windows | None |
| Linux | `apt install libgdiplus libfontconfig1 ttf-mscorefonts-installer` |
| macOS | `brew install mono-libgdiplus` |

## Troubleshooting

**`GroupDocsMetadataException: Could not save the file. Evaluation only.`** -- you are running unlicensed. Apply a license / set `GROUPDOCS_LIC_PATH`.

**`DocumentProtectedException`** -- the document is password-protected. Pass `LoadOptions(password="...")`: `lo = LoadOptions(); lo.password = "..."; Metadata(path, lo)`.

**`System.Drawing.Common is not supported`** -- install libgdiplus: `sudo apt install libgdiplus` (Linux) / `brew install mono-libgdiplus` (macOS)

**`Gdip` type initializer exception** -- outdated libgdiplus: `brew reinstall mono-libgdiplus` (macOS)

**Errors processing images that need fonts** -- install fonts: `sudo apt install ttf-mscorefonts-installer fontconfig && sudo fc-cache -f`

**`DOTNET_SYSTEM_GLOBALIZATION_INVARIANT` errors** -- do NOT set this. Install ICU: `sudo apt install libicu-dev`

**`TypeLoadException`** -- reinstall: `pip install --force-reinstall groupdocs-metadata-net`

**Still stuck?** Post your question at https://forum.groupdocs.com/c/metadata/ -- the development team responds directly.
