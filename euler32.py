import time
from itertools import permutations

def check_permutation(perm):
    multiplicand1 = perm[0]
    multiplicand2 = perm[0] * 10 + perm[1]
    multiplier2 = perm[2] * 100 + perm[3] * 10 + perm[4]
    multiplier1 = perm[1] * 1000 + multiplier2
    product = perm[5] * 1000 + perm[6] * 100 + perm[7] * 10 + perm[8]
    if multiplicand1 * multiplier1 == product or multiplicand2 * multiplier2 == product:
        return product
    return 0

if __name__ == '__main__':
    start = time.time()
    result = sum({check_permutation(perm) for perm in permutations(range(1, 10))})
    print(result == 45228)
    end = time.time()
    print(f"{end-start}")
