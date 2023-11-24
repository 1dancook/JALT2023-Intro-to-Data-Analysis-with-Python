"""
A simple script that generates a table of contents for a jupyter notebook.

As it is, it only generates level 1 and level 2 headers. The first level 1 header will not be included.

One thing that is required within the jupyter notebook is a markdown cell with ONLY this html comment:

    <!-- toc -->

This will be replaced with the markdown version of the table of contents.

This is intended to be used to produce an intermediate notebook before converting to something else like HTML.

Usage: 
    gen-toc.py filename.ipynb
"""

import nbformat
import argparse
from pathlib import Path
from urllib.parse import quote

def convert_to_header_id(header):
    """Convert header contents to valid id value. Takes string as input, returns string. """
    
    # this function is taken from nbconvert but modified slightly
    # I want to keep the behvior of anchor links the same since nbconvert is used to convert the notebook

    # Valid IDs need to be non-empty and contain no space characters, but are otherwise arbitrary.
    # However, these IDs are also used in URL fragments, which are more restrictive, so we URL
    # encode any characters that are not valid in URL fragments.
    return quote(header.replace(" ", "-").replace("*", ""), safe="?/:@!$&'()*+,;=")


# get all of the markdown content
def get_headings(nb, min_level=1, max_level=2):
    for cell in nb["cells"]:
        if cell == nb["cells"][0]:
            continue
        if cell["cell_type"] == "markdown" and cell["source"].startswith("#"):
            heading = cell["source"].split("\n")[0]
            level, heading = heading.split(" ", 1)

            level = len(level)

            if level > max_level or level < min_level:
                continue

            anchor = convert_to_header_id(heading)

            spacing = " " * ((level - 1) * 2)
            bullet = "- "
            header_string = f"{spacing}{bullet}[{heading}](#{anchor})"
            yield header_string

def change_toc_cell(nb):
    toc_cell = None
    for cell in nb["cells"]:
        if cell["cell_type"] == "markdown" and cell["source"].strip() == "<!-- toc -->":
            toc_cell = cell
            break
    headings = get_headings(nb)
    toc_cell["source"] = "## Table of Contents\n\n" + "\n".join([line for line in headings])


def main():
    parser = argparse.ArgumentParser(description="Add TOC to this notebook.")
    parser.add_argument("file_path", help="Path to the file")

    args = parser.parse_args()

    file_path = Path(args.file_path)

    if file_path.exists():

        print("Opening notebook")
        with file_path.open("r") as f:
            nb = nbformat.read(f, as_version=4)

        print("Generating Table of Contents")
        change_toc_cell(nb)

        print("Saving file")
        with open("_temp.ipynb", "w") as f:
            nbformat.write(nb, f)

if __name__ == "__main__":
    main()

