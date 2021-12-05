from elasticsearch import Elasticsearch


def connect_es():
    return Elasticsearch(hosts=["elasticsearch:9200"])


def search_doc(es, data):
    # return es.search(
    #     index=index, body={"query": {"multi_match": {"query": query, "fields": "*"}}}
    # )
    return True
