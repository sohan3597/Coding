#using float statement

from math import sqrt
import math

x = int(input("enter your number: "))
y = float(input("enter your fraction: "))

def fuction_1(x):
    return (sqrt(x+y))

print("square root of x+y is:",fuction_1(x))

def fuction_2(x):
    return ((sqrt(x))+(y/(2*sqrt(x))))

print("of square root of x+y is:",fuction_2(x))

if math.isclose(fuction_1(x), fuction_2(x), rel_tol=1e-9):
    print("the two functions are equal with minimal error f(x+y)-f(x) = f(x) + f'(x)*y is proved")

else :
    print("the two functions are not equal with minimal error f(x+y)-f(x) = f(x) + f'(x)*y is not proved")