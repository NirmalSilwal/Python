def fun():
    print('hello')

fun()


def fun1(ip):
    print('hello',ip)

fun1(888)

import math
def area(r):
    return math.pi * r * r

print('area',area(10))

from math import pi
print(pi)

def isdivisble(num,den):
    if num%den==0:
       return True
    else:
       return False

print(isdivisble(10,2))


