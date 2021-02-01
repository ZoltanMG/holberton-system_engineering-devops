#!/usr/bin/python3
"""
use REST API {JSON} Placeholder
Gather data from an API.
"""


if __name__ == "__main__":
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get("{}users".format(url))
    users = users.json()
    todo = requests.get("{}todos".format(url))
    todo = todo.json()
    data = {}
    for user in users:
        data[user['id']] = []
        for do in todo:
            if do.get('userId') == user['id']:
                data[user['id']].append({'username': user.get('username'),
                                         'task': do.get('title'),
                                         'completed': do.get('completed')})

    name_file = 'todo_all_employees.json'
    with open(name_file, 'w') as json_file:
        json.dump(data, json_file)
