class time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return "The new time is {}:{:02d}:{:02d}".format(self.hour,self.minute,self.second)
    def __add__(self, other_time):
        new_time = time()
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute + other_time.minute

        if (self.hour + other_time.hour) >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time
    def __eq__(self, other):
        if self.hour == other.hour:
            print("Symmetry")
        else:
            print("Not symmetry")


def main():
    time1 = time(1,50,50)
    print(time1)
    time2 = time(1,0,0)
    print(time1 + time2)
    print(time1 == time2)
main()




