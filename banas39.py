with open('with.txt', mode="w", encoding="utf-8") as newfile3:
    newfile3.write('line 1\n line 2 \n line 3')
with open('with.txt', encoding="utf-8") as newfile3:
    print(newfile3.readline())
    while True:
        eachline = newfile3.readline()
        if not eachline:
            break
        print(eachline)
