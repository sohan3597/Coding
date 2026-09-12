#the truth or false game

import math

n = int(input("enter your number: "))

def divides(m, n):
    if m % n == 0:
        return True
    else:
        return False

def even(n):
    return divides(2, n)

def odd(n):
    return not divides(2, n)

print("number is even:", even(n))
print("number is odd:", odd(n))