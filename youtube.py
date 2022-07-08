#  youtubeShort
t1 = (2, -3,-2,-4,-9,2,45,67)
positives = any(m > 0 for m in t1)
print(positives)

checkall = all(m > 0 for m in t1)
print(checkall)