#!/usr/bin/python3
data = input("This is where our input comes from the STDIN: ")
print("Now we write it to the STDOUT: " + data)
raise ValueError("Now we are generating an error to STDERR")

./google70.py < new_file.txt 2> error_file.txt