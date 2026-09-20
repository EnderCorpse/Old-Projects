import random
def genRand(a, b):
    return random.randint(a, b)
genRand = genRand(1, 5)
answer = input("Would you like to know your fortune?")
if answer == "yes":

    if(genRand == 1):
        print("A grand adventure awaits soon.")
    if(genRand == 2):
        print("Someone will help with your troubles.")
    if (genRand == 3):
        print("Wealth awaits, keep track.")
    if (genRand == 4):
        print("Fame awaits, but there's a catch.")
    if (genRand == 5):
        print("Clear skies even with lightning.")
elif answer == "no":
    answer = input("Are you sure?")
    if answer == "yes":
        print("Very well, your loss.")
    if answer == "no":
        if (genRand == 1):
            print("Small wealth will be bestowed.")
        if (genRand == 2):
            print("A small victory will occur today.")
        if (genRand == 3):
            print("You will be visited by an old friend.")
        if (genRand == 4):
            print("An easy day today, for relaxing.")
        if (genRand == 5):
            print("Small fame will come, but only if you wait.")
else:
    print("You have forsaken this place. Be gone at once!")



