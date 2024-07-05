#!/bin/bash
#a script that makes a request which makes the server respond with 'you got me'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
