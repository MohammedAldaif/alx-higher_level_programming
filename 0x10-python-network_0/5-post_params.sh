#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL with variables email and subject, and displays the body of the response
curl -sL -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
