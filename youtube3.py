clist = []
while True:
    srt = input('Enter a new customer details(Yes/No): ')
    srt = srt[0].lower()
    if srt == 'y':
        srt1, srt2 = input("Enter customer both names: ").split()
        clist.append({'m': srt1, 'n':srt2})
    elif srt == 'n':
        print("Successfully registered all entries")
        break
for i in clist:
    print(i['m'],i['n'])
