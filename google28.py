wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for keys,values in wardrobe.items():
	for colors in values:
		print("{} {}".format(colors,keys))