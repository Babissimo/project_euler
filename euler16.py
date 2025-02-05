# sum of digits of 2^1000

#   2   4   8   16  32  64  128 256 512 1024    2048   4096
#   2   4   8   7   5   10  11  13  8   7       14     19


# 303 is slightly more than the length of 2^1000 base 10

digits = [0]* 400

digits[399] = 1

for power in range(1000):
    for index in range(1,400):
        digits[index-1] += (2*digits[index])//10
        digits[index] = (2*digits[index])%10

print(sum(digits))

"""
double largest first





"""