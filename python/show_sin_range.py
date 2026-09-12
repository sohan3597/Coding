import math

def function_1(x):
    return math.sin(x)

# exact points where sin(x) reaches its extrema
print("sin(pi/2) =", function_1(math.pi/2))
print("sin(3*pi/2) =", function_1(3*math.pi/2))
print("Therefore the theoretical range of sin(x) is [-1, +1]")