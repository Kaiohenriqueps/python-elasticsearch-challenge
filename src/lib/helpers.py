from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2, radius):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return True if km <= radius else False


def capture_es_response(es_response):
    return [data.get("_source") for data in es_response.get("hits").get("hits")]


def capture_lat_lon(all_locations, response, radius):
    response_lat_lon = []
    for city in all_locations:
        lat = city.get("lat")
        lng = city.get("lng")
        for elem in response:
            if haversine(elem.get("lng"), elem.get("lat"), lng, lat, radius):
                response_lat_lon.append({"lat": lat, "lng": lng})
    return response_lat_lon

def capture_ids(es, lat_lon):
    response = []
    for elem in lat_lon:
        lat = elem.get("lat")
        lng = elem.get("lng")
        es_response = es.search(index="candidates", body={
            "query": {
                "bool": {
                    "must": [
                        {"match": {"lat": lat}},
                        {"match": {"lng": lng}}
                    ]
                }
            }
        })
        response += [data.get("_source").get("candidate_id") for data in es_response.get("hits").get("hits")]
    return {"ids": response}
    
