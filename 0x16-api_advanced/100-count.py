#!/usr/bin/python3
''' count_words(subreddit, word_list)` function '''
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    ''' count_words(subreddit, word_list)` function '''
    if len(word_dict) == 0:
        for word in word_list:
            word_dict[word] = 0
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    headers = {'User-Agent': 'Python/requests'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            title = child.get('data').get('title')
            for word in word_dict:
                word_dict[word] += title.lower().split(' ').count(word.lower())
        if after is None:
            for key, value in sorted(word_dict.items(),
                                     key=lambda item: item[1],
                                     reverse=True):
                if value != 0:
                    print('{}: {}'.format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dict)
    else:
        return