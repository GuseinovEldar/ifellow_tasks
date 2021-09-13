from math import cos
a = 0
b = 10
e = 0.00001

def func_first(x):
    return cos(pow(x, 5)) + pow(x, 4) - 345.3 * x - 23

def func_second(a, b, e):
    x = (a + b) / 2
    #print(x)
    if (func_first(a) * func_first(x) < 0):
        b = x
    elif (func_first(x) * func_first(b) < 0):
        a = x
    if (abs(b - a) > 2 * e):
        x = func_second(a, b, e)
    return x

x = func_second(a, b, e)

print(x)
