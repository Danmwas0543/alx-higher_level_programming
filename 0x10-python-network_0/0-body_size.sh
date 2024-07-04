#!/bin/bash
#a script which sends a reuquest to a url and displays
#the size of the body of the reponse
curl -s "$1" | wc -c
