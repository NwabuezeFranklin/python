import random
import math

#biglist = [[0] * 10 for i in range(10)]
for i in range(10):
    for j in range(10):
        biglister = "{}:{}".format(i,j)
        print(biglister, end="||")
    print()
