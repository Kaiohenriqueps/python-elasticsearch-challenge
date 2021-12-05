import logging
import haversine as hs
from haversine import Unit


def haversine(lon1, lat1, lon2, lat2, radius):
    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    response = hs.haversine(loc1, loc2, unit=Unit.MILES)
    return True if response <= radius else False


def capture_es_response(es_response):
    return [data.get("_source") for data in es_response.get("hits").get("hits")]


def capture_lat_lon(all_candidates, cities_response, radius):
    response_lat_lon = []
    for city in all_candidates:
        lat = city.get("lat")
        lng = city.get("lng")
        for elem in cities_response:
            if haversine(elem.get("lng"), elem.get("lat"), lng, lat, radius):
                response_lat_lon.append({"lat": lat, "lng": lng})
    return response_lat_lon


def capture_ids(es, lat_lon):
    response = []
    for elem in lat_lon:
        lat = elem.get("lat")
        lng = elem.get("lng")
        es_response = es.search(
            index="candidates",
            body={
                "query": {
                    "bool": {"must": [{"match": {"lat": lat}}, {"match": {"lng": lng}}]}
                }
            },
        )
        response += [
            data.get("_source").get("candidate_id")
            for data in es_response.get("hits").get("hits")
        ]
    return {"candidate_ids": response}
