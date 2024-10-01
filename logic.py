def add(bin_a, bin_b):
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

def subtract(bin_a, bin_b):
    return binary_subtraction(bin_a, bin_b)

def multiply(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    result = 0
    while b > 0:
        if b & 1:
            result = add(bin(result)[2:], bin_a)
        a <<= 1
        b >>= 1
    return bin(result)[2:]

def divide(bin_a, bin_b):
    if bin_b == '0':
        raise ValueError("Cannot divide by zero")
    
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    quotient = 0
    remainder = a

    while remainder >= b:
        temp = b
        multiple = 1
        while remainder >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        remainder = subtract(bin(remainder)[2:], bin(temp)[2:])
        quotient = add(bin(quotient)[2:], bin(multiple)[2:])
    
    return bin(quotient)[2:]
