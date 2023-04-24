#!/usr/bin/python3
"""script uses JSONPlaceholder api to fetch data based on their id
and exports to a csv file"""
import requests
import sys
import csv

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos/?userId={}".format(employee_id)).json()
    # print(type(todos)) # returns a list, if dict, check your params

    # exports to csv block
    with open("{}.csv".format(employee_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # write each task to a new row instead of jamming em up
        for todo in todos:
            writer.writerow([employee_id, user["username"], todo["completed"],
                             todo["title"]])
