# docker stop $(docker ps -aq) 2> /dev/null

# docker rm $(docker ps -aq) 2> /dev/null

# docker network rm asa-net 2> /dev/null

# docker-compose up --build
docker-compose down
docker-compose up --build --remove-orphans
