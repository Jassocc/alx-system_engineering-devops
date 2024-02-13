#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    returns the 10 hottest posts
    """
    headers = ({"User-Agent": "MyRedditClient/1.0"})
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            print("None")
        else:
            for post in posts:
                print(post["data"]["title"])
    else:
        print("None")
