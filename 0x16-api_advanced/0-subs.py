#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers'''


import requests


def number_of_subscribers(subreddit):
    '''f_subscribers(subreddit)'''
    r = requests.get("https://www.reddit.com/r/{}/about.json".
                     format(subreddit), headers={'User-Agent': 'Joa'})
    if r.status_code == 200:
        subscriptions = r.json()["data"]["subscribers"]
        return subscriptions
    else:
        return 0
