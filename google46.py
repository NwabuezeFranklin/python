import re
def check_punctuation (text):
  result = re.search(r"[^a-zA-Z ]", text)
  """ The above expression returns false for all sentences with  only "spaces" and letters capital and  small letters"""
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print(re.findall(r"cats|dogs", "i love cats and dogs Dogs"))
print(re.search(r"cats|dogs[A-Z]", "i love cats and dogs Dogs"))