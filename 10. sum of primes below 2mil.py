numbers=[]

for i in range(1,2*10**6+1):
    numbers.append(i)

for j in range(2,int(2**.5*10**3)+1):
    for n,k in enumerate(numbers):
        if k%j == 0:
            del(numbers[n])

print(sum(numbers))
            
