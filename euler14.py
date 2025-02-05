# longets collatz chain starting below a million
# n -> n/2 if even
# n -> 3n+1 if odd

collatzDistance = {1 : 0}
maxDistance = 0
maxInt = 1

def collatz(n):
    if n == 1:
        return 0
    elif collatzDistance.setdefault(n,0) != 0:
        return collatzDistance[n]
    elif n % 2 == 0:
        return collatz(n//2) + 1
    else:
        return collatz(3*n+1) + 1

for i in range(2,1000001):
    if collatzDistance.setdefault(i,0) == 0:
        if i % 2 == 0:
            collatzDistance[i] = collatz(i//2) + 1
        else:
            collatzDistance[i] = collatz(3*i+1) + 1
    if collatzDistance[i] > maxDistance:
        maxDistance = collatzDistance[i]
        maxInt = i
        
print(maxInt)