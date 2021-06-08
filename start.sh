#!/bin/bash
app="reviewtool"
docker build -t ${app} .
docker run -d -p 8018:80 \
  --name=${app} \
  -v "$PWD:/app" ${app}
