#!/usr/bin/python3
''' como formmat'''


import csv
import requests
import sys
if __name__ == "__main":
    
    user_id = argv[1]
    r1 = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(user_id).json()
    '''load = json.loads(r.text)
    name + load.get("username")'''
    r2 = requests.get('https://jsonplaceholder.typicode.com/todos/?userId={}'.
                     format(user_id).json()
    with open("{}.csv".format(user_id), newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOtE_ALL)
        for task in r2:
            writer.writerow([int(user_id),r1.get('username'),
                             task.get('completed'),
                             task.get('title')])
