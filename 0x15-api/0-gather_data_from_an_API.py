#!/usr/bin/python3
"""
use REST API {JSON} Placeholder
Gather data from an API.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get('{}users/{}'.format(url, id))
    user = user.json()
    name_user = user.get('name')

    url_todo = '{}todos?userId={}'.format(url, id)
    todo = requests.get(url_todo)
    todo = todo.json()
    all_tasks = len(todo)

    url_completed = '{}todos?userId={}&completed=true'.format(url, id)
    all_completed = requests.get(url_completed)
    all_completed = all_completed.json()
    completed_tasks = len(all_completed)

    print('Employee {} is done with tasks({}/{}):'.format(
        name_user,
        completed_tasks,
        all_tasks))
    for do in all_completed:
        print("\t {}".format(do.get('title')))
