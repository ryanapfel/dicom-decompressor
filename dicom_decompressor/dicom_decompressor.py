import os

import click
import pydicom

README_CONTENT = """
# 🖥️ How to Install & Run Brainstorme Imaging Decompression on Mac

## Part 1: One-Time Setup (Python 3.11 & Homebrew)

... (PASTE THE INSTRUCTIONS FROM YOUR EARLIER MARKDOWN FILE HERE) ...
"""


def is_dicom(filepath):
    try:
        pydicom.dcmread(filepath, stop_before_pixels=True)
        return True
    except Exception:
        return False


@click.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False))
def decompress_directory(directory):
    """
    Recursively decompress all DICOM files in a directory.
    Decompressed files are saved with 'DECOMPRESSED-' prefix in the same folder.
    """
    # Set up output directory next to the input root
    output_root = os.path.join(
        os.path.dirname(os.path.abspath(directory)), "decompress"
    )
    os.makedirs(output_root, exist_ok=True)
    decompressed_count = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Skip files that already have DECOMPRESSED- prefix
            if filename.startswith("DECOMPRESSED-"):
                continue
            if not is_dicom(filepath):
                continue
            try:
                ds = pydicom.dcmread(filepath)
                # If not compressed, just skip
                if not ds.file_meta.TransferSyntaxUID.is_compressed:
                    continue
                ds.decompress()
                # Mirror directory structure in output_root
                rel_dir = os.path.relpath(root, directory)
                out_dir = os.path.join(output_root, rel_dir)
                os.makedirs(out_dir, exist_ok=True)
                outpath = os.path.join(out_dir, filename)
                ds.save_as(outpath)
                decompressed_count += 1
                click.echo(f"Decompressed: {filepath} -> {outpath}")
            except Exception as e:
                click.echo(f"Failed to decompress {filepath}: {e}")

    # Write README.md with instructions
    readme_path = os.path.join(directory, "README.md")
    with open(readme_path, "w") as f:
        f.write(README_CONTENT)
    click.echo(f"\nWrote instructions to {readme_path}")
    click.echo(f"\nDecompression complete! {decompressed_count} files processed.")


if __name__ == "__main__":
    decompress_directory()
