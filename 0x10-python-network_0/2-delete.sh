#!/bin/bash
#a script sending a delete request to a url and displays the  response's body
curl -sx "DELETE" "$1"
