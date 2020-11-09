import json

import pytest

from ..app import app


@pytest.fixture
def client(make_test_dir):
    app.config["TESTING"] = True
    app.config["ROOT_DIR_PATH"], _ = make_test_dir 

    with app.test_client() as client:
        yield client


def test_root_request(client):
    response = client.get("/")
    assert b"Wrong request" in response.data


def test_api_request(client):
    response = client.get("/api", follow_redirects=True)
    assert b"Wrong request" in response.data


def test_api_meta_request(client, make_test_dir):
    _, estimated_output = make_test_dir
    response = client.get("/api/meta", follow_redirects=True)
    assert json.loads(response.data) == estimated_output
