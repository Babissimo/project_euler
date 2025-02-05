# 1st triangle number with 500+ divisors

import math

num_of_divisors = {
    1  : 1,
    2  : 2,
    3  : 2,
    6  : 4,
    10 : 4,
    15 : 4,
    21 : 4,
    28 : 6,
}

def countDivisorsTriangle(t, n):
    if n%2 == 0:
        num_of_divisors[n/2] = num_of_divisors.get(n/2, countDivisors(n/2))
        num_of_divisors[n+1] = num_of_divisors.get(n+1, countDivisors(n+1))
        return num_of_divisors[n/2] * num_of_divisors[n+1]
    else:
        num_of_divisors[n] = num_of_divisors.get(n, countDivisors(n))
        num_of_divisors[(n+1)/2] = num_of_divisors.get((n+1)/2, countDivisors((n+1)/2))
        return num_of_divisors[n] * num_of_divisors[(n+1)/2]

def countDivisors(n):
    # count in pairs up to sqrt
    divisorCount = 2
    for i in range(2, int(math.sqrt(n))):
        partnerDivisor = n/i
        if int(partnerDivisor)==partnerDivisor:
            divisorCount += 2
    return divisorCount

nth = 7
tri = 28
found = False


while not found:
    nth += 1
    tri += nth
    num_of_divisors[tri] = countDivisorsTriangle(tri, nth)
    found = num_of_divisors[tri] >= 500

print(tri)