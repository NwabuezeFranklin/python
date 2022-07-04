word1 = input('Enter some words' )
word1  = word1.capitalize()
print(word1)
word2 = word1.split()
print(word2)
list1 = ['unknown', 'battle', 'ground']
word2.extend(list1)
print(type(word2))
print(word2)
for i in word2:
    print(i[0], end="")