import math
x=0
for i in range(1000):
    if i%3 or i%5:
        x+=i
print(math.ceil(x/2))
