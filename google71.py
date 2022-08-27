import sys
for line in sys.stdin:
    print(line.strip().capitalize())


cat new_file.txt | ./google71

./google71 < new_file.txt

