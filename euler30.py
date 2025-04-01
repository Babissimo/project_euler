# sum of numbers expressible as sum of their digits to the power of 5
# 6*9^5 < 999999 so 999999 is an upperbound

def listToInt(digitList):
    return int(''.join(map(str, digitList)))

powerFive = [i**5 for i in range(10)]

# pass down current power sum, current number, current depth. pass up sum of numbers that fit

currentSum = 0
currentNumber = [0] * 6
currentDepth = 0

def calcDigSum(currSum, currNum, currDepth):
    if currDepth < 6:
        totalSum = 0
        currentNum = currNum
        for i in range(10):
            currentNum[currDepth] = i
            totalSum += calcDigSum(currSum + powerFive[i], currentNum, currDepth + 1)
        return totalSum
    elif currSum == listToInt(currNum):
        print(currSum)
        return currSum
    else:
        return 0

print(calcDigSum(0,currentNumber,0)-1)