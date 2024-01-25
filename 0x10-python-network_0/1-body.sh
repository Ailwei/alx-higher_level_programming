#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request and display the body for a 200 status code
if curl -sI "$url" | grep -q "HTTP/1.1 200 OK"; then
    curl -s "$url"
fi
