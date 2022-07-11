class parents:
    def __init__(self, nameFather="OKey", nameMother="Chinyere", House="Duplex"):
        self.__nameFather = nameFather
        self.__nameMother = nameMother
        self.__House = House
    @property
    def nameFather(self):
        return self.__nameFather
    @nameFather.setter
    def nameFather(self, Father):
        self.__nameFather = Father

    @property
    def nameMother(self):
        return self.__nameMother
    @nameMother.setter
    def nameMother(self, Mother):
        self.__nameMother = Mother
    @property
    def House(self):
        return self.__House
    @House.setter
    def House(self, House):
        self.__House = House

    def __str__(self): # type(self).__name__
        return "The Father is {}, mother is {} and they live together in a {}".format(self.__nameFather,self.__nameMother,self.__House)

class children(parents):
    def __init__(self, nameFather="Daddy", nameMother="Mummy", House="Home", siblings='Brothers'):
        parents.__init__(self, nameFather, nameMother, House)
        self.siblings = 'Brothers'
    @property
    def siblings(self):
        return self.__siblings
    @siblings.setter
    def siblings(self, brothers):
        brothers = 'Nonso, Nzube, Chineze, Kosy, Chidera, Chikamso'
        self.__siblings = brothers
    def __str__(self):
        return super().__str__() + " with their 6 children who are {}".format(self.__siblings)
def getit(obb):
    print("the class of {} and their duplex {}".format(type(obb).__name__, obb.House))

def main():

    before = parents()
    print(before.nameFather)
    print(before)
    print()
    after = children()
    print(after)
    getit(before)
    getit(after)


main()