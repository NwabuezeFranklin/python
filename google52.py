import re

print(re.findall(r"[A-Za-z]{5}", "A Crazy ghost around"))

print(re.findall(r"\b[A-Za-z]{5,10}\b", "A Crazy ghost around"))

def long_words(text):
  pattern = r"[A-Za-z]{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

