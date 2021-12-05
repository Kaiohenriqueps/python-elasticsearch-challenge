import ast
import logging
from json import dumps
from flask import Flask, request
from src.lib import crud, helpers

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
        args = request.args.to_dict(flat=False)
        locations = args.get("locations")[0]
        locations = ast.literal_eval(locations)
        radius = int(args.get("radius")[0])
        es = crud.connect_es()
        all_candidates = helpers.capture_es_response(
            crud.search_docs(es, "candidates", {"query": {"match_all": {}}})
        )
        app.logger.info(f"LOCATIONS: {locations}")
        cities_response = helpers.capture_es_response(
            crud.search_docs(es, "cities", {"query": {"terms": {"city": locations}}})
        )
        app.logger.info(f"CITIES RESPONSE: {cities_response}")
        response_lat_lon = helpers.capture_lat_lon(
            all_candidates, cities_response, radius
        )
        app.logger.info(f"RESPONSE: {response_lat_lon}")
        found_ids = helpers.capture_ids(es, response_lat_lon)
        return dumps(found_ids), 200
    except Exception as error:
        error_message = "{}:{}".format(error.__class__.__name__, str(error))
        return error_message, 422


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
