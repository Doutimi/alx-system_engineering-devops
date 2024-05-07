#!/usr/bin/python3
"""Queries the `Reddit API`, prints the titles of the first 10
   hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        result = response.json().get("data").get("children")
        for element in data:
            print(element.get("data").get("title"))
    else:
        print(None)
