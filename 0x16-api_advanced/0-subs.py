#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'ZoltanMG'}
    r = requests.get(url, headers=user_agent, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        data = r.get('data')
        subscribers = data.get('subscribers')
        if subscribers is not None:
            return subscribers
    return 0
