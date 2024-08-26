#!/bin/bash

# Reminder to insert API key
echo "Ensure you have inserted your API key where 'your_api_key_goes_here' is."

# Curl request to fetch quiz questions
curl https://quizapi.io/api/v1/questions -G \
-d apiKey=wRckZ7GSb0fyuFPauV2nv9zPwp2sdcOqZgkBPgdq \
-d limit=10 -o quizoutput.txt

