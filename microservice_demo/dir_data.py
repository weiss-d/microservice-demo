from pathlib import Path
import time
from typing import Any, Dict


def sort_entires(key: Dict[str, str]) -> str:
    """Function for sorting folder items by type and then by name."""
    return (key["type"], key["name"])

def get_dir_data(path: Path) -> Dict[str, Any]:
    """Returns list of files and folders in given directory sorted by type and by name."""
    output_dict = {"data": []}

    for item in path.iterdir():
        if item.is_dir():
            item_type = "folder"
        elif item.is_file():
            item_type = "file"
        else:
            item_type = "unknown"

        output_dict["data"].append(
            {
                "name": item.name,
                "type": item_type,
                "time": time.ctime(item.stat().st_mtime),
            }
        )
    output_dict["data"].sort(key=sort_entires)

    return output_dict
