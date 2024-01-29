#!/usr/bin/python3
"""
using this REST API, for a given employee ID
"""
import json
import requests
import sys


def json_file(employee_id):
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
        employee_name = user_data['username']
        task_list = []
        for task in todos_data:
            task_info = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': employee_name
            }
            task_list.append(task_info)
        user_tasks = {str(employee_id): task_list}
        with open('{}.json'.format(employee_id), mode='w') as json_file:
            json.dump(user_tasks, json_file)
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
    json_file(employee_id)
