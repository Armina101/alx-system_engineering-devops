#!/usr/bin/python3
"""
to get the total number of the subscribers for a particular subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    this function sends a query to the Reddit API and returns the
    total number of subscribers for the particular subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
