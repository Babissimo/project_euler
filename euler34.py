# a curious number is the sum of the factorial of its digits
# eg 145 = 1!+4!+5!

factorials = [1]
factorials = [factorials[-1] for n in range(0, 10) if not factorials.append(max(n,1) * factorials[-1])]

curiousSum = 0

def numberIsCurious(number):
    n = number
    facSum = 0
    while n > 9:
        facSum += factorials[n%10]
        n //= 10
    return number == facSum + factorials[n]


if __name__ == '__main__':

    for i in range(3, 2177281): # big upper bound based on 6 * 9! + 1 as an easy limit
        if numberIsCurious(i):
            curiousSum += i
    print(curiousSum)


# maybe speed gains to be had from avoiding repeated work. dynamic programming?