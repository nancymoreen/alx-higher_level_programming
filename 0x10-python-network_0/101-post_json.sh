#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
