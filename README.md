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