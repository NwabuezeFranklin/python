age = eval(input('Enter your age '))
if age <= 5:
    print('Go to Kindergarten')
elif (age >= 6) or (age <= 17):
    grade = age - 5
    print("Your age is {} Your current grade should be {}".format(age, grade))
else:
    print('Go to college')