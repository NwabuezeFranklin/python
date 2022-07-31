import datetime
import os
# os.remove("what.txt")
# os.rename("Old_file.txt", "New_file.txt")
os.path.exists("guests.txt")
os.path.exists("Not_guests.txt") # File presence

os.path.getsize("guests.txt") # Files_size in Kilobytes
print(os.path.getmtime("guests.txt")) # unix files since the 1970's
timestamp = os.path.getmtime("guests.txt")
datetime.datetime.fromtimestamp(timestamp) # Time can be read and understood

os.path.abspath("guests.txt") # absolute file path
