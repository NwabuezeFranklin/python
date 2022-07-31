import re

print(re.search(r"^A.*a$", "Argentina"))
print(re.search(r"^A.*a$", "Azerbaijan"))


pattern = r"^[A-Z_ ][a-zA-z_]*$"
print(re.search(pattern, "_This_is_a_variabla"))

print(re.search(pattern, " _This_is_a_variable00")) # repair this or make it work :)

patterne = r"^[A-Z][a-zA-Z \?]*$"
print(re.search(patterne, "Is this is a sentence?"))
