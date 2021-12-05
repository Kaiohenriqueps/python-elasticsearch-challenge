import csv
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch(hosts=["elasticsearch:9200"])
es.indices.create(
    index="cities",
    ignore=400,
    body={
        "mappings": {
            "properties": {
                "city": {"type": "keyword"},
                "lat": {"type": "double"},
                "lng": {"type": "double"},
            }
        }
    },
)
es.indices.create(
    index="candidates",
    ignore=400,
    body={
        "mappings": {
            "properties": {
                "candidate_id": {"type": "long"},
                "lat": {"type": "double"},
                "lng": {"type": "double"},
            }
        }
    },
)


with open("./datasets/candidates_locations.csv") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index="candidates")


with open("./datasets/cities_mapping.csv") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index="cities")
