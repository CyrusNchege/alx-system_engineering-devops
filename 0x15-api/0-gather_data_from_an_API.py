#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    """Gather data from an API"""
    user_id = 1
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()
    tasks = []
    for task in todo:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(tasks), len(todo)))
    for task in tasks:
        print("\t {}".format(task))