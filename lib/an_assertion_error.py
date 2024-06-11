#!/usr/bin/env python3

assert(2 + 2 == 4)  

##....
assert(1 == 1)  


##...
def divide(a, b):
    assert b != 0, "The divisor b cannot be zero"
    return a / b

print(divide(10, 2)) 
