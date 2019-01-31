#!/bin/bash

# Run Project
docker-compose up --build -d
sleep 5

# Query results
curl 127.0.0.1:5000/message | jq '.message'
curl 127.0.0.1:5000/status | jq '.'

# Destroy 
docker-compose down
