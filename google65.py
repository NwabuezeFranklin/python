import re

def rearrange_name(name):
    pattern = r"^([\w \.]*), ([\w \.]*)$"
    p=r"^([\w \.]*), ([\w \.]*)$"
    result = re.search(p,name)
    return "{} {}".format(result[2], result[1])


name1 = "Nwabueze N., Franklin"
print(rearrange_name("Chiemerie Stephen., Ifeh"))