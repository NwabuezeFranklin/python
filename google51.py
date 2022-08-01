import re
def rearrange_name(name):
  result = re.search(r"^([\w \.]*), ([\w \.]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Nwabueze . N, Franklin")
print(name)


result = re.search(r"^(\w*) , (\w*)$","John , Kennedy")
print(result[1])