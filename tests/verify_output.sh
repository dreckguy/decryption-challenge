#!/bin/bash
curl 127.0.0.1:5000/status | jq '.' | grep "completed"
curl 127.0.0.1:5000/message | jq '.message' | grep "Great job!"

