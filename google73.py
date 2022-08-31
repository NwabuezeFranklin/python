import re


print(re.search(r"\[(\d+)\]:+ [\w]*", "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))