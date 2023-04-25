#!/usr/bin/python3
"""script uses JSONPlaceholder api to fetch data based on their id
and exports to a csv file"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos/?userId={}".format(employee_id)).json()
    # print(type(todos)) # returns a list, if dict, check your params

    # export to json file code block
    # convert str to dict
    json_dict = {}
    json_dict[employee_id] = []

    # write each data to a new row, think i prefer csv file...
    for todo in todos:
        json_dict[employee_id].append({"task": todo["title"],
                                       "completed": todo["completed"],
                                       "username": user["username"]})

    # dumps (quite literally) the data into a json file, comes last or empty
    # file
    with open("{}.json".format(employee_id), "w") as jsonfile:
        jsonfile.write((json.dumps(json_dict)))
