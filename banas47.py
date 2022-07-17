with open("What.txt",mode="a", encoding="utf-8") as update:
    update.write("\n   Get only one string?\n")
with open("What.txt",mode="r", encoding="utf-8") as update:
    print(update.read())

