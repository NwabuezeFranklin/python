cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for i,j in cool_beasts.items():
    print("{} have {}".format(i,j))

for values in cool_beasts.values():
    print(values)

for keys in cool_beasts.keys():
    print(keys)

for keys,values in cool_beasts.items():
    print("{} are found in {}".format(values,keys))