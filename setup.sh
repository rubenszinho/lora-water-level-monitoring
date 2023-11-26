#!/bin/bash

# Verifica se o argumento --dirty foi passado
if [ "$1" != "--dirty" ]; then
    # Verificar e parar contêineres, se existirem
    for container in mongodb mosquitto; do
        if [ $(docker ps -q -f name=^/${container}$) ]; then
            echo "Parando o contêiner $container"
            docker stop $container
        fi
        if [ $(docker ps -aq -f status=exited -f name=^/${container}$) ]; then
            echo "Removendo o contêiner $container"
            docker rm $container
        fi
    done

    # Verificar e remover a rede, se existir
    if [ $(docker network ls -q -f name=^mqtt-mongo-network$) ]; then
        echo "Removendo a rede mqtt-mongo-network"
        docker network rm mqtt-mongo-network
    fi

    echo "Criando a rede mqtt-mongo-network"
    docker network create mqtt-mongo-network

    echo "Iniciando o contêiner Mosquitto"
    cd mosquitto
    docker run -d --name mosquitto --network mqtt-mongo-network -p 7046:1883 -v $(pwd)/mosquitto/data:/mosquitto/data eclipse-mosquitto
    cd ..

    echo "Iniciando o contêiner MongoDB"
    docker run -d --name mongodb --network mqtt-mongo-network -p 27017:27017 mongo:latest
fi

# Verificar se há atualizações no repositório
cd lora-sensor-website
if git pull | grep -q 'Already up to date.'; then
    echo "Nenhuma atualização encontrada. Não é necessário reconstruir o frontend."
else
    echo "Atualizações encontradas. Reconstruindo o frontend."
    rm -rf ../server-side/build/*
    npm run build
    cp -R build/* ../server-side/build/
fi
cd ..

echo "Construindo e iniciando o contêiner do backend"
cd server-side
if [ $(docker ps -q -f name=^/server-side$) ]; then
    echo "Parando o contêiner server-side"
    docker stop server-side
fi
if [ $(docker ps -aq -f status=exited -f name=^/server-side$) ]; then
    echo "Removendo o contêiner server-side"
    docker rm server-side
fi
echo "Construindo e iniciando o contêiner do lado do servidor"
docker build -t server-side-image .
docker run -d --network mqtt-mongo-network --name server-side -p 8046:5000 server-side-image
cd ..
