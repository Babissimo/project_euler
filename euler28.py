# sum of numbers along diagonals in central spiral 1001*1001 square
# 1 + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25) + (31 + 37 + 43 + 49) + ... + 
# 1 + (4*1^2 + 10*2) + (4*3^2 + 10*4) + (4*5^2 + 10*6) + ... + (4*(n-2)^2 + 10*(n-1))
# 1 + 4*(1^2 + 3^2 + ... + (n-2)^2) + 10*(2 + 4 + ... + (n-1))
# n = 1001
# k = 500
# 1 + 4*(1^2 + 3^2 + ... + (2k-1)^2) + 20*(1 + 2 + ... + k)
# 1 + 4k(2k+1)(2k-1)/3 + 10k(k+1)
# 1 + 4*500*1001*999/3 + 10*500*501
# 669171001