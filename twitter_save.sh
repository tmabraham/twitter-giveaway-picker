#!/bin/sh
while true
do
  python twitter_save_retweets.py
  python twitter_save_likes.py
  sleep 1800
done

