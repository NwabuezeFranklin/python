# exceptions
while True:
    while True:
        try:
            number = int(input('Enter a Number range(0,10) : '))
            break
        except ValueError:
            print('Please Enter a Number : ')
        except:
            print('An unknown error occured, Check your data connection and try again')
    if number == 5:
        print('Congratulations')
        break