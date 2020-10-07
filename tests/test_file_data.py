from pathlib import Path
import time

from microservice_demo import dir_data


def test_get_dir_data(tmp_path):
    test_folder = tmp_path / "test_folder"
    test_folder.mkdir()
    test_subfolder = test_folder / "test_subfolder"
    test_subfolder.mkdir()
    test_another_subfolder = test_folder / "test_another_subfolder"
    test_another_subfolder.mkdir()
    test_file_1 = test_folder / "test_file_1.txt"
    test_file_2 = test_folder / "test_file_2.log"
    test_file_1.write_text("0")
    test_file_2.write_text("01")

    print(test_file_1)
    estimated_output = {
        "data": [
            {
                "name": "test_file_1.txt",
                "type": "file",
                "time": time.ctime(test_file_1.stat().st_mtime)
            },
            {
                "name": "test_file_2.log",
                "type": "file",
                "time": time.ctime(test_file_2.stat().st_mtime)
            },
            {
                "name": "test_another_subfolder",
                "type": "folder",
                "time": time.ctime(test_another_subfolder.stat().st_mtime)
            },
            {
                "name": "test_subfolder",
                "type": "folder",
                "time": time.ctime(test_subfolder.stat().st_mtime)
            },
        ]
    }

    assert dir_data.get_dir_data(test_folder) == estimated_output

