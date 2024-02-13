#!/usr/bin/python3
"""
ueries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    lists all top hot articles
    """
    headers = {"User-Agent": "MyRedditClient/1.0"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url += "&after={}".format(after)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data["data"]["children"]
    if not posts:
        return hot_list
    titles = [post["data"]["title"] for post in posts]
    hot_list.extend(titles)
    next_page = data["data"]["after"]
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    else:
        return hot_list
