# sum all integers not expressible as the sum of 2 abundant numbers
# above 28123 are all expressible as the sum of 2 abundant numbers
#  
# find divisors of numbers
# mark abundant numbers
# sieve numbers for expressibility as 2 abundant numbers
#
# maybe add divisors in pairs?
# perhaps improve last loop
# given the range of i in the first loop dont get why combining with abundant numbers still works. what a wonderful world

def notSumOfTwoAbundants():

    c=28123

    # find sum of divisors and abundant numbers
    aliquotSum = [1]*(c+1)
    abundantNumbers = []
    k = 2
    for i in range(2, c//2+1):
        for j in range(2*i, c+1, i):
            aliquotSum[j]+=i
        if aliquotSum[k] > k:
            abundantNumbers.append(k)
        k += 1
        if aliquotSum[k] > k:
            abundantNumbers.append(k)
        k += 1

    # find numbers inexpressible as the sum of two abundant numbers
    inexpressibles = set(range(1,c+1))
    expressibles = set()
    for (i,m) in enumerate(abundantNumbers):
        for n in abundantNumbers[i:]:
            if m+n > c:
                break
            expressibles.add(m+n)

    return inexpressibles - expressibles

print(sum(notSumOfTwoAbundants()))