from groupdocs.metadata import Metadata


def load_from_stream():
    with open("input.docx", "rb") as stream:
        with Metadata(stream) as metadata:
            # Extract, edit or remove metadata here
            print(f"Loaded {metadata.file_format} from a stream")


if __name__ == "__main__":
    load_from_stream()