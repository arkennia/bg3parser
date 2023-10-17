"""Parse lsx and localization files."""
import os
from pathlib import Path
from typing import Iterator
from lxml import etree


def get_dirs(path: str):
    directories = os.walk(str(Path(path)))
    return directories


def find_files(dirs: Iterator[tuple[str, list[str], list[str]]], extension: str, files: list[str]):
    contents = next(dirs, None)
    if contents:
        f = filter(lambda x: x.endswith(extension), contents[2])
        f = [os.path.join(contents[0], x) for x in f]
        files += f
        return find_files(dirs, extension, files)
    else:
        return files


dirs = get_dirs("../Carian_Knights_Sword")
files = find_files(dirs, ".lsx", [])

x = files[0]

tree: etree._ElementTree = etree.parse(x)
root = tree.getroot()
children = list(root)
for element in root.iter("attribute"):
    print(etree.tostring(element))
