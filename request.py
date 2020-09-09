

import tweepy
import requests


auth = tweepy.OAuthHandler('CdxLDO29YQvSZWNBaTOqEt0rA', 'WzqGijOPtgjNpWRMbSizUgPIWVmSM9RZPtkfNh3KqUGHqbmo1u')
auth.set_access_token('1295350845853315073-F9lV6uj8d3AVypCrkto6UQqgTrqFVj', 'iRYNLQrbiAvO51eqrlKyKqZpFbRNXKixNx4UdzYtFQ8ty')
api = tweepy.API(auth)

payload = {'id': '1303338351290920960'}
r = requests.get("https://twitter.com/Fernanda_Gentil", params=payload)
r.text





