word1 = input('Enter a word: ')
num1 = ''
for i in word1:
    num1 += str((ord(i)-23)+3)
print(num1)
normal = ''
for i in range(0, len(num1)-1, 2):
    recap = num1[i] + num1[i + 1]
    normal += chr(int(recap)+23)
print(normal)