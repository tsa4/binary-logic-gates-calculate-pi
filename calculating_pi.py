#im using a midpoint reimann sum casue the asnwer will be natural numbers
#8/n*sum(k=1 to n, sqrt(k*(n-k))
#        n
#  8    _____
#_____  \          ___________
#  n     /        \|k ( n - k )
#       _____
#        k = 1
from logic import add,subtrac
def binary_search(f, a, b, tol=1e-7):
    if mult(f(a), f(b)) >= 0:
        raise ValueError("Function must have different signs at endpoints a and b.")
    
    while abs(sub(b, a)) > tol:
        mid = (a + b) >> 1
        if mult(f(mid), f(a)) < 0:
            b = mid
        else:
            a = mid

    return (a + b) >> 1

def summation(start, end, function):
    return sum(function(index) for index in range(start, end + 1))

riemann_sqrt = lambda n, k: binary_search(lambda x: mult(x,x)-mult(k,sub(n,k)),1,n)

summation(1,n,riemann_sqrt(n,k))
