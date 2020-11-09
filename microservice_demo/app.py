import os
import sys
from pathlib import Path
import re

from flask import Flask, jsonify
import waitress

from microservice_demo import dir_data


app = Flask(__name__)
app.config.from_pyfile("config.py", silent=True)


@app.after_request
def add_hostname_header(response):
    """Adding location to a response header."""
    env_host = str(os.environ.get("HOSTNAME"))
    hostname = re.findall(r"[a-z]{3}-\d$", env_host)
    if hostname:
        response.headers["SP-LOCATION"] = hostname
    return response


@app.route("/")
def root_url():
    return (
        "Folder data microservice.\nWrong request. Use /api/meta to get directory list."
    )


@app.route("/api")
def api_url():
    return (
        "Folder data microservice.\nWrong request. Use /api/meta to get directory list."
    )


@app.route("/api/meta")
def api_meta_url():
    return jsonify(dir_data.get_dir_data(Path(app.config["ROOT_DIR"])))


if __name__ == "__main__":
    waitress.serve(app, listen="*:5000")
