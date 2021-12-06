#!/bin/sh
# wait-for-postgres.sh

set -e

  
until curl -XGET elasticsearch:9200; do
  >&2 echo "Elastic is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Elastic is up!!"