#im using a midpoint reimann sum casue the asnwer will be natural numbers
#8/n*sum(k=1 to n, sqrt(k*(n-k))
#        n
#  8    _____
#_____  \          ___________
#  n     /        \|k ( n - k )
#       _____
#        k = 1
from logic import add, subtract, divide, multiply
sqrt = binart_search(lambda x: x**2 - multiply(k, subtract(n, k))
def binary_search(f, a, b, tol=1e-7):
    if multiply(f(a), f(b)) >= 0:
        raise ValueError("Function must have different signs at the endpoints.")
    while abs(subtract(b, a)) > tol:
        mid = divide(add(a, b), 2)
        if multiply(f(mid), f(a)) < 0:
            b = mid
        else:
            a = mid
    return divide(add(a, b), 2)

def summation(start, end, function):
    return sum(function(index) for index in range(start, end + 1))

def func_sum(n):
    return summation(1, n, lambda k: sqrt(multiply(k, subtract(n, k))))

def ans(n):
    def riemann(k):
        return multiply(8, divide(func_sum(n), n))
    return binary_search(lambda x: subtract(riemann(x), x), 0, n)

# Example usage:
n = 10  # Replace with your desired value of n
result = ans(n)
print("Approximate square root:", result)
