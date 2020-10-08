from pathlib import Path

from microservice_demo import dir_data


def test_get_dir_data(make_test_dir):
    test_folder, estimated_output = make_test_dir
    assert dir_data.get_dir_data(test_folder) == estimated_output
