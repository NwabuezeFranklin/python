"""
Repetition Modifiers/Qualifiers
"""
import re
print(re.search(r"Py.*n", "Python programming"))
print(re.search(r"Py[a-zA-Z]*n", "Python programming"))
print(re.search(r"o+l+", "woolly"))

print(re.search(r"p?each", "I love peaches")) # This is correct cause p is optional always with the ? symbol

"""
Escaping the special characters using "\"
also \w matches letters, numbers and underscores
others include but not limited to
\d for digits
\s for space and tabs
\
"""
print(re.search(r"\.com", "Gmail.com"))
print(re.search(r"\w*", "tHIS_is_4555_example this was not recgnized due to space btw example and this"))