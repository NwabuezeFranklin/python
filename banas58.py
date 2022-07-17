# Building the multi dimensional list

multi = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print([i[1] for i in multi])

print([multi[i][i] for i in range (len(multi))])

