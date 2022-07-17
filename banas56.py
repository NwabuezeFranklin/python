# Iterables iterators, listcomprehension Generator functions, and Generator  expressions
string1 = iter("String")
print("Just once", next(string1))
print("Just once", next(string1))

class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.letters):
            raise StopIteration
        else:
            self.index += 1
            return self.letters[self.index]
alpha = Alphabet()
for l in alpha:
    print(l)

#print(alpha)

