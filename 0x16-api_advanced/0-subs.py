#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditClient/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        res = response.json().get("data")
        aft = res.get("subscribers")
        return aft
    else:
        return 0
