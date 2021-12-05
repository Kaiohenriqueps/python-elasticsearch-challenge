from elasticsearch import Elasticsearch


def connect_es():
    return Elasticsearch(hosts=["elasticsearch:9200"])


def search_doc(es, index, data):
    return es.search(
        index=index,
        body={"query": {"bool": {"must": [{"terms": {"city": data}}]}}},
    )


def query_all(es, index):
    return es.search(index=index, body={"query": {"match_all": {}}})


def search_docs(es, index, query):
    return es.search(index=index, body=query)
