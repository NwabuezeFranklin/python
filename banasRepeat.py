Password = input('Enter some letters or words, no spaces: ')
code = ''
back = ' '
for i in Password:
    code += str(ord(i))
print('This is the code protect it ',code)
for i in range(0, len(code)-1, 2):
    passcode = code[i] + code[i + 1]
    back += chr(int(passcode))
print(back)

# Check previous files for the mixed script, this is only for capitalized format.


