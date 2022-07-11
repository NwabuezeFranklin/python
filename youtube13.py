

with open('mydata2.txt',mode="w", encoding="utf-8") as demo1:
    demo1.write("This is line 1\n This is line2\n This is line3\n This is line 4\n")
with open("mydata2.txt", encoding="utf-8") as demo1:
    #print(demo1.read())
    while True:
        line = demo1.readline()
        if not line:
            break
        else:
            print(line)