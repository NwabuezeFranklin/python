class demo:
    def __init__(self, practice1="Question1", practice2='Question2'):
        self.practice1 = practice1
        self.practice2 = practice2
    @property
    def practice1(self):
        return self.__practice1
    @practice1.setter
    def practice1(self, value):
        value = input("How many times should one practice(Always/ Never)")
        value = value.lower()
        if value == 'always':
            self.__practice1 = value
            print("You're on the right part")
        else:
            print("You're not on the right part")

    @property
    def practice2(self):
        return self.__practice2

    @practice2.setter
    def practice2(self, value):
        value = input("How many times should one rest(Always/ Never)")
        value = value.lower()
        if value == 'never':
            self.__practice2 = value
            print("You're on the right part")
        else:
            print("You're not on the right part")
    def __str__(self):
        return"Keep Practicing this {}".format(type(self).__name__)
class chad(demo):
    def __init__(self, practice1 = '', practice2="", chadquestion=""):
        demo.__init__(self, practice1, practice2)
        self.chadquestion = chadquestion
    @property
    def chadquestion(self):
        return self.__chadquestion

    @chadquestion.setter
    def chadquestion(self, value):
        value = input("How many girls do you need to survive(None/enter a specific number)")
        value = value.lower()
        if value == 'none':
            self.__chadquestion = value
            print("You're a CHAD")
        else:
            print("You're a SIMP, get lost")
    def mult(self, *args):
        mult =1
        for i in args:
            mult = mult * i
        return mult
def main():
    demo2 = demo()
    #print(demo2.practice1)
    #print(demo2.practice2)
    #print(demo2)
    demo3 = chad()
    #print(demo3.chadquestion)
    print(demo3.mult(2,3,4,5,6))

main()































