try:
    myFile = open('mydata2.txt',encoding="utf-8")
    print(myFile.read())
except FileNotFoundError as faults:
    print("File not found")
    print(faults.args)
else:
    print(myFile.read())
    myFile.close()
    print("Retriving was successful")
finally:
    print("This was fun")

