import os
import subprocess
import sys

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# converted Markdown that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Metadata.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Metadata for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to read, edit, and remove metadata with GroupDocs.Metadata for Python via .NET.
Each example demonstrates different use cases and functionalities such as:

- Reading document, image, audio, and video metadata.
- Searching, setting, adding, and removing properties with predicates and tags.
- Working with EXIF, XMP, and IPTC metadata standards.
- Cleaning (sanitizing) all metadata from a file.
- Exporting metadata to CSV, XLSX, JSON, and XML.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def announce_license():
    """Print whether GROUPDOCS_LIC_PATH points at a usable license file.

    The license itself is applied inside each subprocess by _run_example.py —
    setting it here would only license the runner process, not the children.
    """
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        print(f"{GREEN}License available at: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example as a subprocess via the _run_example.py wrapper.

    Subprocess isolation gives every example a fresh .NET runtime, which
    matters under the current evaluation build: the .NET runtime caps file
    opens at 15 per process, and an in-process runner blows up around the
    16th example. The wrapper also patches Metadata.save so eval-mode save
    errors are logged as notes rather than failing the example.
    """
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)
    wrapper = os.path.join(base_dir, "_run_example.py")

    result = subprocess.run(
        [sys.executable, wrapper, full_path],
        cwd=example_dir,
        env=os.environ.copy(),
    )
    if result.returncode != 0:
        raise RuntimeError(f"subprocess exited with code {result.returncode}")

examples = [
    "getting-started/quick-start-guide/read_metadata.py",
    "getting-started/quick-start-guide/remove_metadata.py",
    "getting-started/quick-start-guide/document_info.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "developer-guide/basic-usage/get-document-info/get_document_info.py",
    "developer-guide/basic-usage/find-metadata-properties/find_metadata_properties.py",
    "developer-guide/basic-usage/remove-metadata-properties/remove_metadata_properties.py",
    "developer-guide/basic-usage/set-metadata-properties/set_metadata_properties.py",
    "developer-guide/basic-usage/clean-metadata/clean_metadata.py",
    "developer-guide/advanced-usage/loading-files/load-from-a-local-disk/load_from_local_disk.py",
    "developer-guide/advanced-usage/saving-files/save-a-modified-file-to-the-original-source/save_file_to_original_source.py",
    "developer-guide/advanced-usage/working-with-metadata-properties/exporting-metadata-properties/exporting_metadata_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/read_basic_exif_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/read_exif_tags.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/read_specific_exif_tag.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/update_exif_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/set_custom_exif_tag.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-exif-metadata/remove_exif_metadata.py",
    "developer-guide/advanced-usage/extracting-metadata/extracting_metadata.py",
    "developer-guide/advanced-usage/loading-files/load-from-a-stream/load_from_stream.py",
    "developer-guide/advanced-usage/saving-files/save-a-modified-file-to-a-specified-location/save_file_to_specified_location.py",
    "developer-guide/advanced-usage/working-with-metadata-properties/extracting-property-values/extract_using_type.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-iptc-iim-metadata/read_basic_iptc_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-iptc-iim-metadata/read_iptc_datasets.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-iptc-iim-metadata/update_iptc_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-iptc-iim-metadata/set_custom_iptc_dataset.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-iptc-iim-metadata/remove_iptc_metadata.py",
    "developer-guide/advanced-usage/loading-files/load-a-file-of-a-specific-format/loading_file_of_specific_format.py",
    "developer-guide/advanced-usage/removing-metadata/removing_metadata.py",
    "developer-guide/advanced-usage/saving-files/save-a-modified-file-to-a-stream/save_file_to_specified_stream.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-xmp-metadata/read_xmp_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-xmp-metadata/update_xmp_properties.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-xmp-metadata/add_custom_xmp_package.py",
    "developer-guide/advanced-usage/working-with-metadata-standards/working-with-xmp-metadata/remove_xmp_metadata.py",
    "developer-guide/advanced-usage/loading-files/load-a-password-protected-document/load_password_protected_document.py",
    "developer-guide/advanced-usage/adding-metadata/adding_metadata.py",
    "developer-guide/advanced-usage/getting-known-property-descriptors/getting_known_property_descriptors.py",
    "developer-guide/advanced-usage/working-with-interpreted-values/working_with_interpreted_values.py",
]

print_intro()
announce_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
