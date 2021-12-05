from elasticsearch import Elasticsearch


def connect_es():
    return Elasticsearch(hosts=["elasticsearch:9200"])


def search_docs(es, index, query):
    return es.search(index=index, body=query)
