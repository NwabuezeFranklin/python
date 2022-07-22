def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.split()[-1] == old:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = [sentence.split()[-1].replace(old, new)]
        new_sentence = sentence.split()[:-1] + i
        new_sentence = " ".join([str(elem) for elem in new_sentence])
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"

