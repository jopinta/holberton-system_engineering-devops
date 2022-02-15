#!/usr/bin/python3
'''use rest api'''


import requests
from sys import argv


if __name__ == "__main__":
    urlTodos = 'https://jsonplaceholder.typicode.com/todos'
    urlUsers = 'https://jsonplaceholder.typicode.com/users'

    r1 = requests.get(urlTodos)
    r2 = requests.get(urlUsers)

    t_json = r1.json()
    u_json = r2.json()

    count = 0
    todos = []
    total = 0
    name = u_json[int(argv[1]) - 1]['name']
    user_id = int(argv[1])

    for user in t_json:
        if user['userId'] == user_id:
            if user['completed']:
                count = count + 1
                todos.append(user['title'])
            total = total + 1

    print('Employee {} is done with tasks({}/{}):'.format(name, count, total))
    for todo in todos:
        print('\t {}'.format(todo))
