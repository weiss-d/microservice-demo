import json

import pytest

from microservice_demo.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_root_request(client):
    response = client.get("/")
    assert b"Wrong request" in response.data


def test_api_request(client):
    response = client.get("/api")
    assert b"Wrong request" in response.data


def test_api_meta_request(client, make_test_dir):
    app.config["ROOT_DIR"], estimated_output = make_test_dir
    response = client.get("/api/meta")
    assert json.loads(response.data) == estimated_output
