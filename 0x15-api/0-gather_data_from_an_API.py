#!/usr/bin/python3
'''use rest api'''


from sys import argv
import requests


if __name__ == "__main__":
    ID = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_list = requests.get('https://jsonplaceholder.typicode.com/users').json()
    count = 0
    todo = []
    total = 0

    for user in user_list:
        if user.get('id') == id:
            name = user.get('name')
            break

    for todo in rx:
        if todo.get('userId') == id:
            if todo.get('completed'):
                todo.append(todo.get('title'))
                count += 1
            total += 1

    print('Emplyee {} is done with tasks({}/{}):'.format(name, todo, total))
    for task in tasks:
        print('\t {}'.format(task))