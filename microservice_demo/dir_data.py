"""
Module for listing a given directory and extracting its contenst metadata.
"""

from pathlib import Path
import time
from typing import Dict, List


def get_dir_data(path: Path) -> List[Dict[str, str]]:
    """Returns list of files and folders in given directory sorted by type and by name.

    Parameters
    ----------
    path : Path
        Path to directory which will be explored.

    Returns
    -------
    List[Dict[str, str]]
        List of dicts that contain file/folder attributes: name, type (file/folder/unknown),
        last modification time.
    """

    output_list = []

    for item in path.iterdir():
        if item.is_dir():
            item_type = "folder"
        elif item.is_file():
            item_type = "file"
        else:
            item_type = "unknown"

        output_list.append(
            {
                "name": item.name,
                "type": item_type,
                "time": time.ctime(item.stat().st_mtime),
            }
        )
    output_list.sort(key=lambda x: (x["type"], x["name"]))

    return output_list
