#im using a midpoint reimann sum casue the asnwer will be natural numbers
#8/n*sum(k=1 to n, sqrt(k*(n-k))
#        n
#  8    _____
#_____  \          ___________
#  n     /        \|k ( n - k )
#       _____
#        k = 1
def bisection_method(func, a, b, tol=1e-7, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    for _ in range(max_iter):
        c = a + (b - a) // 2

        if abs(func(c)) < tol or (b - a) < tol:
            return c

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return a if abs(func(a)) < tol else b

def summation(start, end, function):
    return sum(function(index) for index in range(start, end + 1))
def ans(k):

def binary_search(f, a, b, tol=1e-7):
   if f(a) * f(b) >= 0: raise ValueError()
   while abs(b - a) > tol:
       mid = (a + b) / 2
       a, b = (mid, b) if f(mid) * f(a) < 0 else (a, mid)
   return (a + b) / 2
   
summation(1, n, 
