def factors(n, primes):
    factor = []
    for x in primes:
        while (n % x) == 0:
            factor.append(x)
            n = n/x
    return factor
