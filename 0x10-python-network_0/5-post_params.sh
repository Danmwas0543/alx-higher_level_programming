#!/bin/bash
#a script taking a url sends a post request and displays the respons's body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
