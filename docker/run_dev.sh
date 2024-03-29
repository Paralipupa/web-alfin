#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/..

docker-compose -f docker/docker-compose.dev.yml down
docker rmi $(docker images -aq)
yes | docker system prune
docker-compose -f docker/docker-compose.dev.yml up -d --build


