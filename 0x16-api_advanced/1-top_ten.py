#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers'''


import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts '''
    r = requests.get("https://www.reddit.com/r/{}/about.json".
                     format(subreddit), headers={'User-Agent': 'Joa'})
    if r.status_code == 200:
        subscriptions = r.json()["data"]["children"]
        for title in subscriptions:
            print(title["data"]["title"])
    else:
        print('None')
