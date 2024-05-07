#!/usr/bin/python3
"""Queries the `Reddit API`, prints the titles of the first 10
   hot posts listed for a given subreddit
"""

import requests as r


def top_ten(subreddit):
    """Print top 10 post given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
    }
    param = {
        "limit": 10
    }
    response = r.get(url, headers=headers, params=param, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(top.get("data").get("title")) for top in results.get("children")]
