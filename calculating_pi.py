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
    if f(a) * f(b) >= 0: raise ValueError()
    while abs(b - a) > tol:
        mid = (a + b) / 2
        a, b = (mid, b) if f(mid) * f(a) < 0 else (a, mid)
    return (a + b) / 2
    
