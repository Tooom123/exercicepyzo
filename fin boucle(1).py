##

from random import *


def mystere ():
    m=randint(10,100)
    nombre=0
    while nombre!=m:
        nombre=int(input("choisissez un nombre entre 10 et 100."))
        if nombre<m:
            print ("trop petit :)")
        elif nombre>m:
            print ("trop grand :)")
    print ("Gagné !")

##


def myst ():
    m=randint(10,100)
    nombre=0
    tentative=0
    while tentative!=6:
        while nombre!=m:
            nombre=int(input("choisissez un nombre entre 10 et 100."))
            if nombre<m:
                print ("trop petit :)")
            elif nombre>m:
                print ("trop grand :)")
            tentative=tentative+1
        print ("Gagné !")
    print ("coups épuisés")

##

from math import *
from turtle import *
pas=0
for i in range (10):
    x=randint(-100,100)
    y=randint(-100,100)
    goto(x,y)
    p=sqrt(x**2+y**2)
    pas=pas+p
print (pas)
done()