from pathlib import Path
from flask import Flask, jsonify

from . import dir_data


app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

@app.route("/")
def root_url():
    return "Folder data microservice.\nWrong request. Use /api/meta to get directory list."

@app.route("/api")
def api_url():
    return "Folder data microservice.\nWrong request. Use /api/meta to get directory list."

@app.route("/api/meta")
def api_meta_url():
    return jsonify(dir_data.get_dir_data(Path(app.config["ROOT_DIR"])))
