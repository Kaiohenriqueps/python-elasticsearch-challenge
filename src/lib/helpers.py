import math


def get_distance():
    R = 6373.0

    lat1 = math.radians(52.2296756)
    lon1 = math.radians(21.0122287)
    lat2 = math.radians(52.406374)
    lon2 = math.radians(16.9251681)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
