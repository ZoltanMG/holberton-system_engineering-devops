#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Write a function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'ZoltanMG'}
    r = requests.get(url, headers=user_agent,
                     allow_redirects=False,
                     params={'limit': 10})
    if r.status_code == 200:
        r = r.json()
        data = r.get('data')
        children = data.get('children')
        if data is not None and children is not None:
            for post in children:
                post_data = post.get('data')
                title = post_data.get('title')
                print(title)
    else:
        print('None')
