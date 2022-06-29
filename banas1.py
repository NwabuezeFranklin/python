age = eval(input("Enter your age: "))
if (age >= 1) and (age <= 18):
    print('Important Birthday')
elif(age == 21) or (age == 50) or (age > 65):
    print("Lucky, Important Birthday")
elif (age <= 65):
    print("Not found")


