friends = {
    'Nonso': '23',
    'Chris': '34',
    'folak': '27',
}
print(friends['Chris'])
print(friends)
print('Chris' not in friends)
friends.popitem()   # friends.pop(indicate is better)
print(friends)
friends.keys()
print(friends.keys())
print(friends.get('Chris'))
friends.clear()
print(friends)