#!/bin/bash
#a script sending a json request to a url and diplay the response's body
curl -s -H "content-Type: application/json" -d "$(cat $2)" "$1"
