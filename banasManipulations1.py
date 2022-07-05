sample = 'Treat as Important'
for i in range(0, len(sample)-1, 2):
    print(sample[i] + sample[i+1])

for i in range(0, len(sample)-1):
    print(int(ord(sample[i])))
