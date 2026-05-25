import io

from groupdocs.metadata import Metadata


def save_file_to_specified_stream():
    stream = io.BytesIO()
    with Metadata("input.png") as metadata:
        # Edit or remove metadata here
        metadata.sanitize()
        metadata.save(stream)

    print(f"Saved {stream.getbuffer().nbytes} bytes to the stream")


if __name__ == "__main__":
    save_file_to_specified_stream()