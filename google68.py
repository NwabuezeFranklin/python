my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

import random

participants = ['Jack', 'Jill', 'Larry', 'Tom']


def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False


print(Guess(participants))

# The code seems to be working fine. However, there are some things that could go wrong, so find the part that might throw an exception and wrap it in a try-except block to ensure that you get sensible behavior. Do this in the cell below. Code your function to return None if an exception occurs.

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))