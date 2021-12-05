import logging
from src.lib import crud_es
from json import loads, dumps
from flask import Flask, render_template, request

app = Flask(__name__)


flask_logger = logging.getLogger(__name__)


@app.route("/")
def home():
    return "hello world!"


@app.route("/search/<string:my_index>/<string:query>", methods=["GET"])
def search_doc(my_index: str, query: str):
    try:
        es = crud_es.connect_es()
        response_search = crud_es.search_doc(es=es, index=my_index, query=query)
        flask_logger.info("doc has been searched!")
        flask_logger.info(dumps(response_search))
        return response_search, 200
    except Exception as error:
        error_message = "{}:{}".format(error.__class__.__name__, str(error))
        flask_logger.error(error_message)
        return error_message, 422


if __name__ == "__main__":
    app.run(host="0.0.0.0")
