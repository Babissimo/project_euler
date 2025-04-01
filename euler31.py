# how many ways to make £2 in coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200]

numOWaysToMakeN = [0] * 201
numOWaysToMakeN[0] = 1

for c in coins:
    for i in range(c, 201):
        numOWaysToMakeN[i] += numOWaysToMakeN[i-c]

print(numOWaysToMakeN[200])