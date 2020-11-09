import logging
import re
from string import Template
import os
from pathlib import Path

from flask import Flask, jsonify
import waitress

from microservice_demo import dir_data


app = Flask(__name__)
app.config.from_pyfile("config.py", silent=True)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%d-%m-%y %H:%M:%S",
)

ROOT_DIR = Path(app.config["ROOT_DIR"])

# Templates are used instead of string interpolation for security reasons.
LOGGING_INFO_FOLDER_PROCESSING = Template(
    "Done processing request for folder: $folder."
)
LOGGING_INFO_FOLDER_ERROR = Template("ERROR in processing $folder: $error.")

if not ROOT_DIR.exists():
    logging.warning("WARNING: Root directory specified in config.py doesn't exist.")


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


@app.route("/api/meta/<folder>")
def api_meta_url(folder):
    try:
        response = dir_data.get_dir_data(ROOT_DIR / folder)
        logging.info(LOGGING_INFO_FOLDER_PROCESSING.substitute(folder=folder))
    except Exception as e:
        e = str(e)
        response = {"error": e}
        logging.info(LOGGING_INFO_FOLDER_ERROR.substitute(folder=folder, error=e))
    return jsonify(response)


if __name__ == "__main__":
    waitress.serve(app, listen="*:5000")
