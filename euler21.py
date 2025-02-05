# 2 numbers are amicable if their proper divisors sum to each other
# ie 220's divisors sum to 284 and 284's sum to 220
# sum all amicable numbers under 1000

# 1000
# 2^3 * 5^3
# 1, 2, 4, 8, 5, 25, 125, 10, 50, 250, 20, 100, 500, 40, 200
# 1320
# 2^3 * 3 * 5 * 11
# 1, 2, 4, 8, 3, 6, 12, 24, 5, 10, 20, 40, 11, 22, 44, 88, 15, 30, 60, 120, 

'''
make list of set of proper divisors
make list of sum of proper divisors
if amicable add to running total
'''

properDivisors = {2 : {1}}
properDivisorSum = {2 : {1}}
amicableSum = 0

def findProperDivisors(n):
    divisors = {1}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors

def amicable(n):
    nDivisors = properDivisors.setdefault(n, findProperDivisors(n))
    nDivisorSum = properDivisorSum.setdefault(n, sum(nDivisors))
    pDivisors = properDivisors.setdefault(nDivisorSum, findProperDivisors(nDivisorSum))
    pDivisorSum = properDivisorSum.setdefault(nDivisorSum, sum(pDivisors))
    return n == pDivisorSum != nDivisorSum

for i in range(3,10000):
    
    # test the amicability
    if amicable(i):
        amicableSum += i

print(amicableSum)