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
    headers = {"User-Agent": "MyBot/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response status code:", response.status_code)
    print("Response content:", response.content)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
