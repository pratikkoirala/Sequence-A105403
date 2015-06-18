from A105403_checker import *
def A105403(N):
    result = []
    primes = prime_list()
    for x in xrange(1, N):
        if A105403_checker(x, primes):
            result.append(x)
    return result
