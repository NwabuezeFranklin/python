#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list
employee_list = read_employees('/home/student-02-eafceeafe220/data/employees.csv')
print(employee_list)
def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data
dictionary = process_data(employee_list)
print(dictionary)

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k) + ':' + str(dictionary[k]) + '\n')
                f.close()
write_report(dictionary, '/home/student-02-eafceeafe220/data/report.txt')

"""
The goal of the script is to read the CSV file and generate a report with the total number of people in each department. To achieve this, we will divide the script into three functions.



Let's start with the first function: read_employees(). This function receives a CSV file as a parameter and returns a list of dictionaries from that file. For this, we will use the CSV module.



The second function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount.

Next, we will write the function write_report. This function writes a dictionary of department: amount to a file.

The report should have the format:

<department1>: <amount1>

<department2>: <amount2>
"""