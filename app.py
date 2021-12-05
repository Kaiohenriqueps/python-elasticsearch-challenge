import logging

import flask
from src.lib import crud, helpers
from json import dumps
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(
    filename="record.log",
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


@app.route("/")
def home():
    return "hello world!"


@app.route("/search", methods=["GET"])
def search_doc():
    app.logger.info("Info level log")
    app.logger.warning("Warning level log")
    try:
        # es = crud.connect_es()
        locations = request.args.get("locations")
        radius = request.args.get("radius")
        return request.args, 200
    except Exception as error:
        error_message = "{}:{}".format(error.__class__.__name__, str(error))
        flask_logger.error(error_message)
        return error_message, 422


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
