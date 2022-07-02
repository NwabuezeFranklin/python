words = input('Convert to Acronym: ')
words = words.upper()
list = words.split()
print(list)
for i in list:
    print(i[0], end="")

