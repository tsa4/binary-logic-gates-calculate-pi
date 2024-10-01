def add(a,b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return bin(a)[2:]
    
def binary_subtraction(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return bin(a)[2:]
    
def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
    
def subtract(a, b):
    return add(a, add(~b, 1))
    
def multiply(a, b):
    result = 0
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)
    while b > 0:
        if b & 1:
            result = add(result, a)
        a <<= 1
        b >>= 1
    return -result if negative else result
    
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    negative = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)
    quotient = 0
    while a >= b:
        temp = b
        multiple = 1
        while a >= (temp << 1):
            temp <<= 1
            multiple <<= 1
