class school:
    def __init__(self,student="", teachers=""):
        self.student = student
        self.teachers = teachers

class library(school):
    def __init__(self, registration):
        super().__init__(student="", teachers="")
        self.registration = registration