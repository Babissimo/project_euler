# find d < 1000 s.t. 1/d has longest recurrence

# store fractions

def isRecurringFromNPeriodR(d,leadingSize,periodSize):

    # if leading digits removed and recurring with period size
    if (10 ** leadingSize / d) // 1 == (10 ** (leadingSize+periodSize) / d) // 1:
        return True
    else:
        return False

def period(d):
    periodFound = False
    i = 1
    while not periodFound:
        for j in range(i-1,-1,-1):
            if isRecurringFromNPeriodR(d, j, i-j):
                return i-j
        i += 1

maxPeriod = 1
maxD = 1

for d in range(2,1000):
    p = period(d)
    if p > maxPeriod:
        maxPeriod = p
        maxD = d

print(d)