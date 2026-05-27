"""Internal helper: run a single example with eval-mode save() made non-fatal.

`run_all_examples.py` invokes this wrapper for each example as a separate
subprocess. Two things this gives us under the current evaluation limits:

  * **Fresh .NET runtime per example.** The evaluation build caps file opens
    at 15 *per process*, so the previous in-process runner would explode at
    around example #16. A new subprocess resets the counter for every run.

  * **Save-time eval errors are non-fatal.** Without a license, every
    `metadata.save(...)` raises ``GroupDocsMetadataException: ... Evaluation
    only.``. The wrapper monkey-patches ``Metadata.save`` so this specific
    exception is logged as a note and treated as success — the example still
    demonstrates the API. With a license applied, the patch is a no-op.

The wrapper also self-applies the license from ``GROUPDOCS_LIC_PATH`` if it
is set in the environment (the parent runner exports it but does not call
``License().set_license`` in-process, because that would only affect the
parent, not the subprocesses).

Usage (from ``run_all_examples.py``)::

    python Examples/_run_example.py <path/to/example.py>
"""
from __future__ import annotations

import os
import runpy
import sys

from groupdocs.metadata import License, Metadata


def _apply_license() -> None:
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        try:
            License().set_license(license_path)
        except Exception:
            # If the license can't be applied (corrupted, expired, etc.) just
            # fall back to evaluation mode — the save() guard below handles it.
            pass


def _install_save_guard() -> None:
    original_save = Metadata.save

    def safe_save(self, *args, **kwargs):
        try:
            return original_save(self, *args, **kwargs)
        except Exception as exc:
            if "Evaluation only" in str(exc):
                target = args[0] if args else "<original source>"
                print(
                    f"Note: save to {target} skipped — evaluation mode "
                    f"(apply a license to enable save())."
                )
                return None
            raise

    Metadata.save = safe_save


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: _run_example.py <example.py>", file=sys.stderr)
        return 2

    _apply_license()
    _install_save_guard()

    runpy.run_path(argv[1], run_name="__main__")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
