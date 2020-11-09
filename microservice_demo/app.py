"""
Simple demo of microservice in Flask.

Personal project for learning Flask and Docker.

The app returns a list of files and folders and some of their properties
from given subdirectory of a directory specified in 'cofig.py'.

    $ pip install -r requirements.txt
    $ python -m microservice_demo.app
"""
import logging
import os
import re
from string import Template

from flask import Flask, jsonify
from flask.wrappers import Response
import waitress

from microservice_demo import dir_data


# Initializing Flask app and logging


app = Flask(__name__)
app.config.from_pyfile("config.py", silent=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%d-%m-%y %H:%M:%S",
)

if not app.config["ROOT_DIR_PATH"].exists():
    logging.warning("WARNING: Root directory specified in 'config.py' doesn't exist.")

# Templates are used instead of string interpolation for security reasons.
LOGGING_INFO_FOLDER_PROCESSING = Template(
    "Done processing request for folder '$folder'."
)
LOGGING_INFO_FOLDER_ERROR = Template("ERROR in processing '$folder': $error.")


@app.after_request
def add_hostname_header(response: Response) -> Response:
    """Adding Docker container info to a response header for debugging possibilities.

    Parameters
    ----------
    response : Response
        Initial Flask response.

    Returns
    -------
    Response
        Flask response with added Docker container info.

    """
    env_host = str(os.environ.get("HOSTNAME"))
    hostname = re.findall(r"[a-z]{3}-\d$", env_host)
    if hostname:
        response.headers["SP-LOCATION"] = hostname
    return response


# Routes


@app.route("/")
@app.route("/api/")
def root_url() -> str:
    """Root API route. No functions.

    Returns
    -------
    str
        Error and message about API usage.

    """
    return "Folder data microservice.\nWrong request. Use /api/meta/<folder> to get folder list."


@app.route("/api/meta/")
def api_meta_url() -> Response:
    """Base API route. Returns data of the configured root folder.

    Returns
    -------
    Response
        List of file/forder data of the rood directory specified in 'config.py' in JSON format.

    """
    logging.info(
        LOGGING_INFO_FOLDER_PROCESSING.substitute(folder=app.config["ROOT_DIR_PATH"])
    )
    return jsonify({"data": dir_data.get_dir_data(app.config["ROOT_DIR_PATH"])})


@app.route("/api/meta/<path:folder>")
def api_meta_folder_url(folder: str) -> Response:
    """Main API route for retrieving data for subfolders.

    Parameters
    ----------
    folder : str
        Any level subfolder of a root forlder.

    Returns
    -------
    Response
        List of file/folder data of given subfolder in JSON format.

    """
    abs_folder = app.config["ROOT_DIR_PATH"] / folder
    try:
        response = {"data": dir_data.get_dir_data(abs_folder)}
        logging.info(LOGGING_INFO_FOLDER_PROCESSING.substitute(folder=abs_folder))
    except Exception as e:
        e = str(e)
        response = {"error": e}
        logging.info(LOGGING_INFO_FOLDER_ERROR.substitute(folder=abs_folder, error=e))
    return jsonify(response)


if __name__ == "__main__":
    waitress.serve(app, listen="*:5000")
