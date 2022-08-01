import re

print(re.split(r"[?.!]","This is sentence a. This is sentence b? This is the last sentence!"))

print(re.split(r"([?.!])","This is sentence a. This is sentence b? This is the last sentence!")) # With the associate  dividers

print(re.sub(r"[\w-]+@[\w.-]*","[PRIVATE]", "Recieved an email from nwafrank2017@gmail.com on Today"))