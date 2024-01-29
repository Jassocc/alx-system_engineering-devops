#!/usr/bin/python3
"""
using this REST API, for a given employee ID
"""
import requests
import sys


def employee_todo_list(employee_id):
    """
    gets the list with id
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}users/{}'.format(base_url, employee_id)
    todos_url = '{}todos?userId={}'.format(base_url, employee_id)
    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        completed_tasks = [task for task in todos_data if task['completed']]
        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completion_count = len(completed_tasks)
        print('Employee {} is done with tasks({}/{}):'.format(employee_name,
              completion_count, total_tasks))
        for task in completed_tasks:
            print('\t {}'.format(task["title"]))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    employee_todo_list(employee_id)
