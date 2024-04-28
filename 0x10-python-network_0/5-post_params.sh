#!/bin/bash
# Send a post req with parameters email=test@gmail.com&subject=I will always be here for PLD
curl -sd "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
