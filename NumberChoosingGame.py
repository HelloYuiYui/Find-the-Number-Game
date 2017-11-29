
import time
from random import randint
import random
from time import sleep

print ("Hello, I am an harmless space creature")
time.sleep(2.0)
print("I just wanted to play a game")
time.sleep(1.0)

def findTheNumber():
    print ("Between which numbers we should choose a number?")
    num1 = int(input("number 1: "))
    num2 = int(input("number 2: "))
    game = random.randint(num1, num2)
    print ("choose a number between" + str(num1) + " and " + str(num2))
    count = 0
    while True:
        count += 1
        answer = int(input("num: "))
        if answer < oyun:
            print ("up")
        elif answer > oyun:
            print ("down")
        else:
            print ("we have found it!")
            print ( "you have tried for" + str(count) + "times")
            time.sleep(10.0)
            break

findTheNumber()
