import os
# os.mkdir("Alpha")
# os.chdir('Alpha')
print(os.getcwd())
with open('new.txt', mode="w", encoding='utf-8') as myfile2:
    myfile2.write('This is line 1\n This is line 2\n This is line 3\n This is line 4\n This is the last line')
with open('new.txt',encoding="utf-8")as myfile2:
    print(myfile2.readline())
    while True:
        liner = myfile2.readline()
        if  not liner:
            break
        print(liner)

