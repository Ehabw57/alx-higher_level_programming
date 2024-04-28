#!/bin/bash
# send a OPTION request the first arg of the script
curl -sI "$1" | grep "Allow" | cut -b 8-
