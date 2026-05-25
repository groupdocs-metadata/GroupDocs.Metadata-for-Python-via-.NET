from groupdocs.metadata import Metered


def set_metered_license():
    public_key = "*****"  # Your public key
    private_key = "*****"  # Your private key

    # Guard the sample so it doesn't call the API with placeholder keys
    if "*" in public_key or "*" in private_key:
        print("Provide your real metered keys to activate metered licensing.")
        return

    # Activate metered (pay-as-you-go) billing for this process
    Metered().set_metered_key(public_key, private_key)
    print("Metered license set successfully.")


if __name__ == "__main__":
    set_metered_license()