import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  # result =re.search(r"A.E.I", text, re.IGNORECASE)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


# practice all about grep