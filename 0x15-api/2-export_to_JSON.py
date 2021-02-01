#!/usr/bin/python3
"""
use REST API {JSON} Placeholder
Gather data from an API.
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get('{}users/{}'.format(url, id))
    user = user.json()
    name_user = user.get('username')

    url_todo = '{}todos?userId={}'.format(url, id)
    todo = requests.get(url_todo)
    todo = todo.json()

    data = {str(id): []}
    for do in todo:
        data[str(id)].append({'task': do.get('title'),
                              'completed': do.get('completed'),
                              'username': name_user})
    name_file = '{}.json'.format(id)
    with open(name_file, 'w') as json_file:
        json.dump(data, json_file)
