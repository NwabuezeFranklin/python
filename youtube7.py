ent, age, sex = input("Enter your name,age and sex").split()
age = int(age)
sex = sex[0].lower()

if sex == 'm':
    if age > 35:
        print("this was late and undeserved")
    elif age <= 35 and age >= 18:
        print("You should be in the university or College")
    elif age > 0 and age < 4:
        m = age -1
        while m < 4:
            print("You should be in nursery{}".format(m))
            break
    elif age >= 4 and age < 9:
        m = age - 3
        while m < 7:
            print("you should be in primary {}".format(m))
            break
    elif age >= 10 and age < 14:
        m = age - 9
        while True:
            print("you should be in Jss {}".format(m))
            break
    elif age >= 14 and age < 17:
        m = age - 13
        while True:
            print("you should be in SSS {}".format(m))
            break
    elif age >= 17 and age <= 18:
        print("You should be writing either Waec or Jamb or both")

elif sex == 'f':
    if age > 35:
        print("You should be married")
    elif age <=28 and age >= 35:
        print("Hope your are in a healthy relationship, Start making plans for marriage")
    elif age <=27 and age >= 23:
        print("Charm a spouse and get ready for marriage, Take your time,Start making plans for marriage")
    elif age <=24 and age >= 18:
        print("You should be in the University or College")
    elif age > 0 and age < 4:
        m = age -1
        while m < 4:
            print("You should be in nursery{}".format(m))
            break
    elif age >= 4 and age < 9:
        m = age - 3
        while m < 7:
            print("you should be in primary {}".format(m))
            break
    elif age >= 10 and age < 14:
        m = age - 9
        while True:
            print("you should be in Jss {}".format(m))
            break
    elif age >= 14 and age < 17:
        m = age - 13
        while True:
            print("you should be in SSS {}".format(m))
            break
    elif age >= 17 and age <= 18:
        print("You should be writing either Waec or Jamb or both")

else:
    print("Enter your name, age and sex in this order and appropriately, (sex = Male/Female)")




