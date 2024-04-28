#!/bin/bash
# send a GET req to the first arg of the script with header var X-School-User-Id=98
curl -sH "X-School-User-Id:98" "$1"
