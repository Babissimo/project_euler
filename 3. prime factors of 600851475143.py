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

print(prime_factorisation(600851475143))
