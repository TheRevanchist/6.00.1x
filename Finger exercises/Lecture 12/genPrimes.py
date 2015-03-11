def genPrimes():
    primes = []
    num = 1
    
    while True:
        num += 1
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
            yield num
            