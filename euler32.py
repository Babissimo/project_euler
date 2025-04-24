import time
from itertools import permutations

def check_permutation(perm):
    multiplicand = perm[0] * 10 + perm[1]
    multiplier = perm[2] * 100 + perm[3] * 10 + perm[4]
    product = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
    if multiplicand * multiplier == product:
        return product
    multiplier += perm[1] * 1000
    if perm[0] * multiplier == product:
        return product
    return 0

if __name__ == '__main__':
    start = time.time()
    result = sum({check_permutation(perm) for perm in permutations(range(1, 10))})
    print(result == 45228)
    end = time.time()
    print(f"{end-start}")
