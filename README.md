# python-elasticsearch-challenge
Project with Python and Elasticsearch.

## Pre requisites
1) Install Docker
2) Install docker-compose

## Interacting with the projects
1) Start the project using the command:
```
$ docker-compose up -d
```
  1.1) If you want to see if the services are online, check the logs using the command:
```
$ docker-compose logs -f <service_name>
```
2) You can input the data using flask's URL:
```
localhost:5000/search?locations=["San Francisco","New York"]&radius=50
```

## About the challenge

### What you’ll get:
You will be given two datasets that you can download from Assets.

1) cities_mapping.csv contains city names and their corresponding longitude and latitude
2) candidates_locations.csv contains candidate ID and the longitude and latitude corresponding to their location

### What you’ll do:

1) You will create an index in ElasticSearch v7.15
2) You will ingest given datasets (at least one) into an index that you just created in ElasticSearch
3) You will write a code to perform a search on the ElasticSearch index to find a list of candidate ids which fulfill the above ask given the user input
4) Your solution should be able to take user input which will be a list of cities and an integer value representing distance. The result should be a list of candidate ids which are located within the user input distance from any one of the cities in the user input list

Example User input:
```
locations: [“San Francisco”, “New York”, “London”] radius: 50
```

Example Output:
```
candidate_ids = [110011, 110022, 230023, ...]
```
In other words, it should return a list of candidate ids which are within 50 miles from any given city in the list.