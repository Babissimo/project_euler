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

all_de_factors=[]
for i in range(1,21):
    all_de_factors=all_de_factors+prime_factorisation(i)
print(all_de_factors)

#forget it
