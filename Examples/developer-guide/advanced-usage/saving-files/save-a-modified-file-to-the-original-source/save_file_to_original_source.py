from groupdocs.metadata import Metadata


def save_file_to_original_source():
    with Metadata("input.ppt") as metadata:
        # Edit or remove metadata here
        removed = metadata.sanitize()
        print(f"Removed {removed} properties")

        # Saves the document back to the underlying source (stream or file)
        metadata.save()


if __name__ == "__main__":
    save_file_to_original_source()