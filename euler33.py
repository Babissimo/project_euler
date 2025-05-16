# 49/98 = 4/8 is non-trivial
# 30/50 = 3/5 is trivial
# 4 non-trivial  examples < 1 w/ 2 digs in num & denom
# multiply these 4 fractions, simplify and return denominator

for denominator in range(12, 100):
    denTens = denominator // 10
    denUnit = denominator % 10
    for numerator in range(11, denominator):
        numTens = numerator // 10
        numUnit = numerator % 10
        if denTens == denUnit and numTens == numUnit or numUnit == denUnit == 0 or numUnit * denTens == numTens * denUnit:
            continue
        # if n/d == nT/dT | nU/dT | nT/dU | nU/nT
        if numerator * denTens == numTens * denominator and numUnit == denUnit:
            print(f"{numerator}/{denominator}={numTens}/{denTens}")
        elif numerator * denTens == numUnit * denominator and numTens == denUnit:
            print(f"{numerator}/{denominator}={numUnit}/{denTens}")
        
        if numerator * denUnit == numTens * denominator and numUnit == denTens:
            print(f"{numerator}/{denominator}={numTens}/{denUnit}")
        elif numerator * denUnit == numUnit * denominator and numTens == denTens:
            print(f"{numerator}/{denominator}={numUnit}/{denUnit}")