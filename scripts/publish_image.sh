#!/bin/bashs
IMAGE=dreckguy/decryption
#travis env handling to docker***
touch .env
echo  "ENCRYPTED_FILE_ADDRESS=$ENCRYPTED_FILE_ADDRESS" >> .env
echo "SECRET_KEY=$SECRET_KEY" >> .env
#image creation
docker build -t $IMAGE .
  - docker login --username $DOCKER_USER --password $DOCKER_PASSWORD
  - docker push $IMAGE