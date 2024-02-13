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
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "MyRedditClient/1.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get('data')
        subscribers = data.get('subscribers')
        return subscribers
    except requests.exceptions.RequestException as e:
        return 0
