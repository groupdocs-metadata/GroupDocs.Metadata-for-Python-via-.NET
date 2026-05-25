from groupdocs.metadata import Metadata


def clean_metadata():
    # Open the file to clean
    with Metadata("input.pdf") as metadata:
        # sanitize() removes every detected metadata property in one call
        affected = metadata.sanitize()
        print(f"Properties removed: {affected}")
        # Write the cleaned document to a new file
        metadata.save("output.pdf")


if __name__ == "__main__":
    clean_metadata()