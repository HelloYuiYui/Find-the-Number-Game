
import time
from random import randint
import random
from time import sleep

print ("Selam dostlar. Ben zararsız bir uzay canlısıyım.")
time.sleep(2.0)
print("Bugün sizlerle bir oyun oynamak için buradayım.")
time.sleep(1.0)

def rakamsecmece():
    print ("hangi rakamlar arasında bir rakam sallayalım?")
    rakam1 = int(input("rakam 1: "))
    rakam2 = int(input("rakam 2: "))
    oyun = random.randint(rakam1, rakam2)
    #print (oyun)
    print (str(rakam1) + " ile " + str(rakam2) + " arasi bir rakam secin.")
    count = 0
    while True:
        count += 1
        cevap = int(input("rakam: "))
        if cevap < oyun:
            print ("yukarı, daha yukarı")
        elif cevap > oyun:
            print ("aşağı, en diplere")
        else:
            print ("Tamamdır, bulduk")
            print ("you have tried for" + str(count) + "times")
            break

rakamsecmece()

"""
an experiment to check that we are able to compare within strings

a = 5
str(a)
b = 6
str(b)
if a<b:  
    print ("oh")
else:
    print ("yandık")
"""