import math

def calculation(x):
    function1 = math.cos(2*x)
    function2 = -2*math.sin(2*x)
    function3 = -4*math.cos(2*x)
    return function1, function2, function3

print(calculation(math.pi))