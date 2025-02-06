x = 1
for x in range(997):
    for y in range(x):
        if ((x**2+y**2)**0.5)%1 == 0:
            if x + y + ((x**2+y**2)**0.5) == 1000:
                print(x*y*(x**2+y**2)**0.5)
