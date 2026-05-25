from groupdocs.metadata import Metadata


def getting_known_property_descriptors():
    with Metadata("input.doc") as metadata:
        root = metadata.get_root_package()
        # Not every package exposes document properties; guard for it
        document_properties = getattr(root, "document_properties", None)
        if document_properties is not None:
            # Each descriptor describes a known property the package supports
            for descriptor in document_properties.know_property_descriptors:
                print(descriptor.name)          # property name
                print(descriptor.type)          # value type
                print(descriptor.access_level)  # read-only / read-write

                # Tags attached to the property (used by the search predicates)
                for tag in descriptor.tags:
                    print(tag)

                print()


if __name__ == "__main__":
    getting_known_property_descriptors()