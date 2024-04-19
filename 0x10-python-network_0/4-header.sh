#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
# A header variable X-HolbertonSchool-User-Id must be sent with the value 98

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request with a custom header and display the response body
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
