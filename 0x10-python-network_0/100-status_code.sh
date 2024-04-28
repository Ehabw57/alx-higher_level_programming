#!/bin/bash
# Display only the http status code of the last responde
curl -Is --write-out "%{http_code}" -o /dev/null "$1"
