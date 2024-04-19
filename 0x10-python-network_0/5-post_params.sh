#!/bin/bash
# This script sends a POST request to a URL with specified variables and displays the response body

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract URL from command line arguments
url="$1"

# Define variables for email and subject
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with specified variables and display the response body
curl -s -X POST -d "email=$email&subject=$subject" "$url"
