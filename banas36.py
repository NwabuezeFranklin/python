import os
with open('What.txt', mode="w", encoding="utf-8") as myfile:
    myfile.write("This is a new file i just started working on\n You can create a new line using the old trick from c\n Remember that you get only one string" )
with open('what.txt', encoding="utf-8") as myfile:
    print(myfile.read())
    print(myfile.read())

print(myfile.closed)
print(myfile.name)
#  os.rename('What.txt', 'Whatif.txt')
#  os.remove
print(myfile)
#  os.mkdir("newdir")
print("My current working directory: ",os.getcwd())