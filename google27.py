def count_dict(tests):
    result = {}
    for letter in tests:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

to_print  =count_dict("This wa vneiurbver erfjreijbvri z")
print(to_print)