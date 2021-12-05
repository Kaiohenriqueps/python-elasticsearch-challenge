import logging

import flask
from src.lib import crud, helpers
from json import dumps
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


@app.route("/")
def home():
    return "hello world!"


@app.route("/search", methods=["GET"])
def search_doc():
    try:
        args = request.args.to_dict()
        locations = args.get("locations")
        radius = args.get("radius")
        es = crud.connect_es()
        all_locations = helpers.capture_es_response(
            crud.search_docs(es, "cities", {"query": {"match_all": {}}})
        )
        response = helpers.capture_es_response(
            crud.search_docs(
                es, "cities", {"query": {"bool": {"must": [{"terms": {"city": locations}}]}}}
            )
        )
        response_lat_lon = helpers.capture_lat_lon(all_locations, response, radius)
        found_ids = helpers.capture_ids(es, response_lat_lon)
        return dumps(found_ids), 200
    except Exception as error:
        error_message = "{}:{}".format(error.__class__.__name__, str(error))
        return error_message, 422


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
