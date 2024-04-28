#!/bin/bash
# Display only the http status code of the last responde
curl -Is --write-out "%{http_code}\n" -o /dev/null "$1"
