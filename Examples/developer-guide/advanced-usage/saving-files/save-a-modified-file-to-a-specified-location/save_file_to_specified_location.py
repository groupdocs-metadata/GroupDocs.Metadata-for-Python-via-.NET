from groupdocs.metadata import Metadata


def save_file_to_specified_location():
    with Metadata("input.jpg") as metadata:
        # Edit or remove metadata here
        removed = metadata.sanitize()
        print(f"Removed {removed} properties")

        metadata.save("output.jpg")


if __name__ == "__main__":
    save_file_to_specified_location()