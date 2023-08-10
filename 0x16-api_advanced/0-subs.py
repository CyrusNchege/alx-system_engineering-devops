#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''returns the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
