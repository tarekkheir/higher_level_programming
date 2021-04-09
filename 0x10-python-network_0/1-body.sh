#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sI "$1" -X GET -w "%{http_code}" -eq 200
