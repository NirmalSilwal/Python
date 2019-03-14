import math

def fact(n):
    return math.factorial(n)

def mainFunction():
    for i in range(1,21,1):
        print(i,":",fact(i))
mainFunction()