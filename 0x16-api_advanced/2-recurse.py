#!/usr/bin/python3
''' queries the Reddit API and returns the number of subscribers'''


import requests


def recurse(subreddit, hot_list=[], after=0):
    '''Listings and share five common parameters'''
    r = requests.get("https://www.reddit.com/r/{}/hot.json".
                     format(subreddit), headers={'User-Agent': 'Joa'})
    if r.status_code != 200:
        return None
    try:
        hot_list.append(r.json()["data"]["children"][after]["data"]["title"])
    except IndexError:
        return hot_list
    return recurse(subreddit, hot_list, after+1)
