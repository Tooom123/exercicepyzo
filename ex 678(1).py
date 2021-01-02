from turtle import *
from random import *
def tracecarre():
    for i in range (4):
        forward(20)
        left(90)


##


def dixcarres():
    for i in range (10):
        ((tracecarre(20)))


def dixcarresbis():
    for i in range (10):
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(20)
        left(90)
        forward(30)

##
def dixcarresbisbis():
    n=10
    for i in range (10):
        n = n + 5
        forward(n)
        left(90)
        forward(n)
        left(90)
        forward(n)
        left(90)
        forward(n)
        left(90)
        up()
        forward(n+10)
        down()





##

def dixcarresbisbisbis():
    n=10
    listecouleur= ["red","blue","yellow","green","brown","pink","black","purple","cyan","maroon"]
    for i in range (10):
        c=randint(1,10)
        couleur=listecouleur[c]
        color(couleur)
        n = n + 5
        forward(n)
        left(90)
        forward(n)
        left(90)
        forward(n)
        left(90)
        forward(n)
        left(90)
        up()
        forward(n+10)
        down()

    done()


##


def damier():
    x=0
    for i in range (5):
        x=x+10
        goto(x,0)
        tracecarre(20)

    done()

##

def infini():
    for i in range (1000):
        print ("coucoucoucoucoucoucoucoucou")




















