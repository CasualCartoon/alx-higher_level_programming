#!/bin/bash
# This script sends a POST request to a URL with specified email and subject variables using curl

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request with email and subject variables and display the response body
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
