# F_1 = 1, F_2 = 1,
# F_n = (phi^n-(1-phi)^n)/sqrt5
# 1st F_n over 1000 digits

# 1000 <= log(F_n)


import math

previous = 1
current = 1
temp = 1
index = 2

while math.log10(current) < 999:
    index += 1
    temp = current
    current += previous
    previous = temp

print(index)