palindromes=[]
for i in range(100,1000):
    for j in range(100,i+1):
        if str(i*j)==str(i*j)[::-1]:
            palindromes.append(i*j)
print(max(palindromes))
