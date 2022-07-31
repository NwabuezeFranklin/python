with open("csv_file.txt","w") as file:
    file.write("Eric Cartman, 0000-2222-555, Standup-comedian\n Kylie Mendy, 0000-555-3333, Accontant\n Nwabueze Franklin, 0817-462-3477, IT Specialist")
with open("csv_file.txt","r+")as file:
    print(file.read())

import csv

file = open("csv_file.txt")
file1 = csv.reader(file)
for row in file1:
    name,phone,role = row
    print("Name: {}, Phone:{}, Role:{}".format(name,phone,role))
file.close()

