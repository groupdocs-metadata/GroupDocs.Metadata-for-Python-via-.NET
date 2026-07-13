# GroupDocs.Metadata for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-metadata-python-net-banner.png)](https://releases.groupdocs.com/metadata/python-net/)

[Product Page](https://products.groupdocs.com/metadata/python-net/) | [Docs](https://docs.groupdocs.com/metadata/python-net/) | [Demos](https://products.groupdocs.app/metadata/family) | [API Reference](https://reference.groupdocs.com/metadata/python-net/) | [Blog](https://blog.groupdocs.com/category/metadata/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/metadata) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Metadata for Python via .NET](https://products.groupdocs.com/metadata/python-net/) is a metadata management API that reads, edits, and removes metadata from documents, images, audio, and video — supporting XMP, EXIF, IPTC, Image Resource Blocks, ID3, and document properties across 110+ file formats.

## Features

- **110+ formats**: Read, edit, and remove metadata in Microsoft Office, PDF, images, audio, video, archives, and more.
- **Metadata Standards**: XMP, EXIF, IPTC IIM, Image Resource Blocks, and ID3 (ID3v1/ID3v2), Lyrics3, APE.
- **Search Engine**: Find, update, add, and remove properties with simple Python predicates and predefined tags.
- **One-Call Sanitize**: Strip every detected property before sharing a file.
- **Document Inspection**: Detect format/MIME type, page count, and encryption.
- **Export**: Dump the metadata tree to CSV, XLSX, JSON, or XML.
- **On-Premise**: No cloud or internet connection required.

## Supported File Formats

GroupDocs.Metadata for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, Image, Email, and many others. See the [full list of supported formats](https://docs.groupdocs.com/metadata/python-net/supported-document-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.5+](https://www.python.org/downloads/) is installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-metadata/GroupDocs.Metadata-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Metadata-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/metadata/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_metadata_net-26.5-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: `run_all_examples.py` automatically applies a license when one is available, looking in two places:

   - The `GROUPDOCS_LIC_PATH` environment variable — set it to the absolute path of your `.lic` file (recommended).
   - Any `*.lic` file in the repository root.

   With a license applied, examples run with the full feature set; without one, output documents carry an evaluation watermark and are capped at the first two pages. Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   You can also run individual examples by navigating to the folder containing the example script and running it. Output files are placed in the same folder as the script file.

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the .NET runtime dependencies (`libicu-dev`), and the `groupdocs-metadata-net` package preinstalled.

```bash
# Build the image
docker build -t metadata-examples .

# Run unlicensed (evaluation mode)
docker run --rm metadata-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    metadata-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-metadata-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/metadata/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting.

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/metadata/python-net/agents-and-llm-integration/) page for the per-tool setup snippets.

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Metadata for Python via .NET documentation](https://docs.groupdocs.com/metadata/python-net/).

We also offer **GroupDocs.Metadata** packages for other platforms:
* [**GroupDocs.Metadata for .NET**](https://products.groupdocs.com/metadata/net/)
* [**GroupDocs.Metadata for Java**](https://products.groupdocs.com/metadata/java/)
* [**GroupDocs.Metadata for Node.js via Java**](https://products.groupdocs.com/metadata/nodejs-java/)

---

[Product Page](https://products.groupdocs.com/metadata/python-net/) | [Docs](https://docs.groupdocs.com/metadata/python-net/) | [Demos](https://products.groupdocs.app/metadata/family) | [API Reference](https://reference.groupdocs.com/metadata/python-net/) | [Blog](https://blog.groupdocs.com/category/metadata/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/metadata) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
