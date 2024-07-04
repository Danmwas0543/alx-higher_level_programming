#!/bin/bash
#a script which sends a reuquest to a url
curl -s "$1" | wc -c
