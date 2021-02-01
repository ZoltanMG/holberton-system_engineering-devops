#!/usr/bin/python3
"""
use REST API {JSON} Placeholder
Gather data from an API.
"""


if __name__ == "__main__":
    import csv
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

    name_file = '{}.cvs'.format(id)
    with open(name_file, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for do in todo:
            csv_writer.writerow(["{}".format(id),
                                "{}".format(name_user),
                                "{}".format(do.get('completed')),
                                 "{}".format(do.get('title'))])
