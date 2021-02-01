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
    name_user = user.get('username')

    url_todo = '{}todos?userId={}'.format(url, id)
    todo = requests.get(url_todo)
    todo = todo.json()

    name_file = '{}.csv'.format(id)
    with open(name_file, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for do in todo:
            csv_writer.writerow([str(id),
                                name_user,
                                do.get('completed'),
                                do.get('title')])
