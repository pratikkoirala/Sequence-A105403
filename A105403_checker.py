from compare_function import *
from factor_function import *

def is_prime(n, primes):
    if n > 1:
	      sqrt = int(n ** 0.5)
        for x in primes:
              if x > sqrt:
		              return True
            if (n % x) == 0:
                return False
        return True
    else:
        return False

def prime_list():
    list_prime = [2]
    for x in xrange(3, 7*10**6, 2):
        if is_prime(x, list_prime):
            list_prime.append(x)
    return list_prime

def nth_prime(n, primes):
    return primes[n - 1]

def A105403_checker(n, primes):
    first_number = nth_prime(n, primes) - 1
    second_number = nth_prime(n + 1, primes) - 1

    first_factors = factors(first_number, primes)
    second_factors = factors(second_number, primes)

    if (len(first_factors) > 0) and (len(second_factors) > 0):
        if first_factors[-1] == second_factors[-1]:
            return True
    else:
        return False

