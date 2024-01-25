#!/bin/bash
# Get the content-length of a given IP addresses
curl -sI "$1" | awk '/Content-Length/{print $2}'
