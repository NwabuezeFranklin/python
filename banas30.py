customerlist = []
while True:
    str = input('Enter new customer (Yes/no): ')
    str = str[0].lower()
    if str == 'y':
        str1, str2 = input('Enter both names of customer: ').split()
        customerlist.append({'m':str1,'n':str2})
    elif str == 'n':
        print('Ok we are done here')
        break
for i in customerlist:
    print(i['m'],i['n'])


