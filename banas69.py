while True:
    try:
        ent = input("Enter a number: ")

        ent = int(ent)
        if ent == 4:
            print("Congratulations, Game Over")
            break
        elif ent > 4:
            print("Guess lower")
        elif ent < 4:
            print("Guess higher")
    except ValueError:
        print("Enter only numerical values")
    except:
        print("Unknown Error")