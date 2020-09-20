from typing import Dict

import tweepy
import requests
import os
from dotenv import load_dotenv

with open('texto.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#load_dotenv('credential.txt')
#token = os.getenv('TWEET TOKEN')
token = 'AAAAAAAAAAAAAAAAAAAAAEpzGwEAAAAAA%2FhnALfeo3F%2BE%2FAvWwhJc4ZIdC0%3DhaMkykSFgVQZVzO4fmkehk903U5b5JSuZgq78RW3x5kMCTWttc'
id = '1307786611095040000'
headers = {'Authorization': f'Bearer {token}'}
r = requests.get(url=f"https://api.twitter.com/2/tweets/{id}", headers=headers)
print(r.text)
