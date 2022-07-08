#  tutorial from youtube
l = (1,2,3,4,5)
m = ("one","two","Three", "four")
for i,j in zip(l,m):
    print(i,j)
print()


# normal procedure
list1 = [1,2,3,4,5]
list = ['one', 'two', 'three', 'four', 'five']
for i in range(len(list)):
    print(list1[i],list[i])

#  Some dictionary recap
dict ={
    'henry': 'one',
    'franklin': 'two',
}
dict['isdore'] = 'Third'
print(dict['henry'])
print(dict)
print(dict.keys())
print('henry' not in dict)
for i  ,j in dict.items():
    print(i,j)