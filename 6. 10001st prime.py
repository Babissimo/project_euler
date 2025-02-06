def prime_factorisation(val):
    prime_factors = []
    i = 2
    while i ** 2 <= val:
         while val % i == 0:
             val /= i
             prime_factors.append(i)
         i += 1
    prime_factors.append(int(val))
    try:
        prime_factors.remove(1)
    except ValueError:
        pass
    return prime_factors

x=[]
i=1
while len(x)<10001:
    i+=1
    if len(prime_factorisation(i))==1:
        x.append(i)
print(x[-1])

