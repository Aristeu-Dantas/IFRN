#!/bin/bash

echo "Criando imagens..."

docker build -t c01 -f c01/Dockerfile c01/

docker build -t c02 -f c02/Dockerfile c02/

docker build -t c03 -f c03/Dockerfile c03/

docker build -t proxy -f Dockerfile.proxy .

docker image ls

echo "Criando a rede..."

docker network create -d bridge asa-net

echo "Criando conteiners..."

docker run -dp 8001:80 --name c01 c01

docker run -dp 8002:80 --name c02 c02

docker run -dp 8003:80 --name c03 c03
