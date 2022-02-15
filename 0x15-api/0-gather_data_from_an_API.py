#!/usr/bin/python3
'''use rest api'''


from sys import argv
import requests


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
    name = response[int(argv[1]) - 1]['name']

    for user in user_list:
        if user.get('id') == id:
            name = user.get('name')
            break

    for todo in response:
        if todo.get('userId') == id:
            if todo.get('completed'):
                todo.append(todo.get('title'))
                count += 1
            total += 1

    print('Emplyee {} is done with tasks({}/{}):'.format(name, todo, total))
    for todo in todos:
        print('\t {}'.format(todo))
