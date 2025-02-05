# f(n) = n^2 + an + b
# starting n = 0, find (a,b) s.t. most consecutive primes in f(n)
# return a*b

# f(n) != 2
# f(0) = b so b is prime so b is 3 or 6k+-1 so b is odd so a is odd.
# f(1) = a + b + 1 if prime then a + b + 1 >= 3 then a >= 2 - b

def checkPrime(n):
    pass

mostPrimes = 0
bestA = 0
bestB = 0

#test b = 3
for b in range(6, 998, 6):
    # b+1
    # b-1
    for a in range(2-b, 1000, 2):
        nPrime = True
        n = 0
        while nPrime:
            nPrime = checkPrime(n)
            n += 1
        n -= 1
        if n > mostPrimes:
            mostPrimes = n
            bestA = a
            bestB = b

print(a*b)