import time

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


def prime_list(N):
    list_prime = [2]
    for x in xrange(3, N, 2):
        if is_prime(x, list_prime):
            list_prime.append(x)
    print len(list_prime)
    return list_prime


def nth_prime(n, primes):
    return primes[n - 1]

def greatest_prime_factor(n, primes):
    factor = 1
    for x in primes:
        while (n % x) == 0:
            n = n/x
            factor = x
        if n == 1:
            break
    return factor


def A105403_checker(n, primes):
    first_number = nth_prime(n, primes) - 1
    second_number = nth_prime(n + 1, primes) - 1
    
    first_factor = greatest_prime_factor(first_number, primes)
    second_factor = greatest_prime_factor(second_number, primes)

    if first_factor == second_factor:
        return True
    else:
        return False


def A105403(N):
    result = []
    num = int(raw_input("Enter upper bound for prime list:"))
    start = time.time()
    primes = prime_list(num)
    for x in xrange(1, N):
        if A105403_checker(x, primes):
            result.append(x)
    stop = time.time()
    print stop - start
    return result

