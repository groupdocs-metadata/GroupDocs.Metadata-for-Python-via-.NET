from groupdocs.metadata import Metadata


def working_with_interpreted_values():
    with Metadata("input.jpg") as metadata:
        # Keep only properties that expose a human-readable interpreted value
        properties = metadata.find_properties(lambda p: p.interpreted_value is not None)
        for prop in properties:
            print(prop.name)
            print(prop.value.raw_value)              # original (raw) value
            print(prop.interpreted_value.raw_value)  # friendly interpretation
            print()


if __name__ == "__main__":
    working_with_interpreted_values()