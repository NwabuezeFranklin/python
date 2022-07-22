def pig_latin(text):
    say = ""
    fill = []
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        string = word[1:] + word[0] + 'ay'
        # Turn the list back into a phrase
        fill.append(string)
    say = " ".join([str(m) for m in fill])
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"