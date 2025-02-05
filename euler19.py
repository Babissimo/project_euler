'''
    num of sundays on the first of the month between Jan 1 1901 - Dec 31 2000
    1 Jan 1900 = Monday.
'''

thirtyMonths = [3,5,8,10]
thiryOneMonths = [0,1,4,6,7,9,11]

# firstDay = [1901, 0, 1] # where 1 is Tuesday

# leap year on years divisible by 4, but not by 100 unless by 400
def isLeapYear(year):
    return year%4 == 0 & (year%100 != 0 | year%400 == 0)

def yearLength(year):
    return 365 + isLeapYear(year)

def monthLength(month, year):
    if month in thirtyMonths:
        return 30
    if month in thiryOneMonths:
        return 31
    return 28 + isLeapYear(year)

dayOfWeek = 1
sundayCount = 0
for year in range(1901, 2001):
    for month in range(12):
        sundayCount += dayOfWeek == 6
        dayOfWeek += monthLength(month, year)
        dayOfWeek %= 7

print(sundayCount)