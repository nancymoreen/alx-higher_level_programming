#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET requestto the URL
curl -s -H "X-School-User-Id:98" "$1"
