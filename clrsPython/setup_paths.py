"""
Setup script for CLRS Python chapter imports.

Run this once (with your virtual environment activated) to create a .pth file
that adds all CLRS chapter folders to Python's import path. This allows the
cross-chapter imports (e.g., Chapter 22 importing from Chapter 10) to work.

Usage:
    python clrsPython/setup_paths.py
"""

import site
import sys
from pathlib import Path


def main():
    clrs_root = Path(__file__).resolve().parent

    # Collect all chapter and utility directories.
    dirs = sorted(
        [p for p in clrs_root.iterdir() if p.is_dir() and not p.name.startswith(".")],
        key=lambda p: p.name,
    )

    if not dirs:
        print("Error: No chapter directories found.")
        sys.exit(1)

    # Find site-packages inside the active virtual environment.
    site_packages = site.getsitepackages()
    if not site_packages:
        print("Error: Could not find site-packages. Is your virtual environment activated?")
        sys.exit(1)

    pth_path = Path(site_packages[0]) / "clrs_paths.pth"
    lines = [str(d) for d in dirs]

    pth_path.write_text("\n".join(lines) + "\n")
    print(f"Created {pth_path} with {len(lines)} entries:")
    for line in lines:
        print(f"  {line}")


if __name__ == "__main__":
    main()
