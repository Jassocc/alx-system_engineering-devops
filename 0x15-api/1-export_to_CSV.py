#!/usr/bin/python3
"""
using this REST API, for a given employee ID
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    exports to csv
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
        with open('{}.csv'.format(employee_id), mode='w',
                  newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                          'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow({
                    'USER_ID': str(employee_id),
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': str(task['completed']),
                    'TASK_TITLE': task['title']
                })
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
    export_to_csv(employee_id)
