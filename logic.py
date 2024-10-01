def add(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return bin(a)[2:]

def sub(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    b = ~b + 1
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return bin(a)[2:]

def mult(bin_a, bin_b):
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return bin(result)[2:]

def div(bin_a, bin_b):
    if bin_b == '0':
        raise ValueError("Division by zero is not allowed")
    a = int(bin_a, 2)
    b = int(bin_b, 2)
    quotient = 0
    remainder = 0
    for i in range(len(bin_a)):
        remainder = (remainder << 1) | ((a >> (len(bin_a) - 1 - i)) & 1)
        if remainder >= b:
            remainder -= b
            quotient |= (1 << (len(bin_a) - 1 - i))
    return bin(quotient)[2:], bin(remainder)[2:]
