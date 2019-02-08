import time
from random import randint
import random
from time import sleep

print ("Hello, I am an harmless space creature")
time.sleep(2.0)
print("I just wanted to play a game")
time.sleep(1.0)

#defines findTheNumber function
def findTheNumber():
    print ("Between which numbers I should choose a number?")
    #creates variables called number 1 and number 2
    num1 = int(input("number 1: "))
    num2 = int(input("number 2: "))
    #creates a random number between chosen numbers
    game = random.randint(num1, num2)
    print ("choose a number between" + str(num1) + " and " + str(num2))
    #creates count variable for count the loop
    count = 0
    #creates a loop until you find the number chosen
    while True:
        count += 1
        answer = int(input("num: "))
        if answer < game:
            print ("up")
        elif answer > game:
            print ("down")
        else:
            print ("you have found it!")
            print ( "you have tried for " + str(count) + " times")
            time.sleep(10.0)
            break

findTheNumber()
