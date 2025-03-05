
###use of memo
memo={}
def binomial_coeff(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)
    memo[(n,k)]=res
    return res
#print(binomial_coeff(4,2))

###using default
from functools import lru_cache
@lru_cache(None)
def binomial_coeff(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)
    return res
#print(binomial_coeff(4,2))

##conditional expression
from functools import lru_cache
@lru_cache(None)
def binomial_coeff(n, k):
    return 1 if k==0 else (0 if n==0 else (binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)))
print(binomial_coeff(100, 45))
