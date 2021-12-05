import csv
from elasticsearch import Elasticsearch, helpers

# Create the elasticsearch client.
es = Elasticsearch(hosts=["localhost:9200"])
es.indices.create(index="candidates", ignore=400)
es.indices.create(index="cities", ignore=400)

# Open csv file and bulk upload
with open("./datasets/candidates_locations.csv") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index="candidates")


with open("./datasets/cities_mapping.csv") as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index="cities")
