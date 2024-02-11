import os
import sys
import random
import time

def wait(i):
    i = int(i)
    time.sleep(i)
    
dead = random.randint(1, 6)

print("Do you want to play russian roulette?: Y/N")
anwser = str(input("> "))

if anwser.lower() == "y":
    print("The rules are simple.")
    wait(2)
    print("Press ENTER To Shoot")
    wait(2)
    print("There's one 'bullet'")
    wait(2)
    print("And there are 5 blanks")
    wait(2)
    print("You gonna die if in chamber there's the bullet")
    wait(2)
    print("How long do you want to spin? (1-10)")
    amount = int(input("> "))
    print("Spinning.")
    if amount < 11:
        for i in range(0, amount):
            chamber = random.randint(1, 6)
        print("Do You Want To Shoot?")
        wait(2)
        print("Y - Shoot")
        print("N - Skip")
        shoot_anwser = str(input("> "))

    if shoot_anwser.lower() == "n":
        if chamber == dead:
            print("You've Missed Your Death!")
        else:
            print("That Was A Blank.")
    elif shoot_anwser.lower() == "y":
        if chamber == dead:
            print("You've died!. Removing python file")
            file_name =  os.path.basename(sys.argv[0])
            os.remove(file_name)
        else:
            print("That Was A Blank.")
