# f(n) = n^2 + an + b
# starting n = 0, find (a,b) s.t. most consecutive primes in f(n)
# return a*b

# f(n) != 2
# f(0) = b so b is prime so b is 3 or 6k+-1 so b is odd so a is odd.
# f(1) = a + b + 1 if prime then a + b + 1 >= 3 then a >= 2 - b

mostPrimes = 0
bestAB = (0, 0)
primeList = {2, 3, 5, 7}

def checkPrime(p):
    if p in primeList:
        return True
    if p < 1: 
        return False
    for i in range(12, int(p**1/2)+6):
        if p%(i-1) == 0 or p%(i+1) == 0:
            return False
    primeList.add(p)
    return True
    

def testB(b):
    global mostPrimes
    global bestAB
    for a in range(2-b, 1000, 2):
            nPrime = True
            n = -1
            f = b
            while nPrime:
                n += 1
                nPrime = checkPrime(f)
                f += a + 2*n + 1
            if n > mostPrimes:
                mostPrimes = n
                bestAB = (a, b)

testB(3)
for c in range(6, 997, 6):
    # b is c+-1
    testB(c-1)
    testB(c+1)


print(bestAB[0]*bestAB[1])