#!/usr/bin/python3
"""script uses JSONPlaceholder api to fetch data based on their id"""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos/?userId={}".format(employee_id)).json()
    # print(type(todos)) # returns a list, if dict, check your params

    # code block fetches all completed task, adds them to the list done_tasks
    done_todos = []
    for i in todos:
        if i.get("completed") is True:
            done_todos.append(i)

    print("Employee {} is done with tasks({}/{}):"
          .format(user["name"], len(done_todos), len(todos)))
    for todo in done_todos:
        print("\t", todo["title"])
