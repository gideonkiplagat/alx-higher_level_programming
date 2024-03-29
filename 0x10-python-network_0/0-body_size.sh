#!/bin/bash
# script to get the body size of a request
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
