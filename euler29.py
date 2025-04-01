"""
how many distinct values for a^b for all 2 <= a,b <= 100
if 2 <= a^b <= 100 then family of duplicates to discount
eg 2^2 = 4 so discount all 4^k = 2 ^ 2k where 2k <= 50

    2   3   4   5   6   7   8   9   10  11
2   4   8   
3
4
5
6
7
8
9
10
11

basic idea is count smaller a's first. if they overlap with bigger a's then for the bigger a's count from where the smaller a can't reach.
ie 2^b overlaps with 4^b. 2^100 is its max. so it can reach 4^50. so start counting for 4 at 4^51 and go on
2^3 is 8. 2^99 is max. 8^33
2^4 is 16. 2^100 is max. 16^25
4^2 is 16. 4^100 is max. 16^50
10^2 is 100. 10^100 = 100^50.
7^2 is 49. 7^100 = 49^50
2^6 = 64. 2^96 = 64^16
4^4 = 64. 4^100 = 64^25
8^2 = 64. 8^100 = 64^50
2^5 = 32. 2^100 = 32^20
"""

distinctVals = 99*99
bStartsAfter = [1] * 101
for a in range(2, 101):
    b = 2
    aPowB = a*a
    while aPowB <= 100: # discount duplicates by updating bStartsAfter
        bStartsAfter[aPowB] = 100//b # bStartsAfter 100//b as highest a**bk s.t. bk <= 100
        b += 1
        aPowB *= a
    distinctVals -= bStartsAfter[a] # count what's left and add to distinctVals
print(distinctVals)

# under by 5. unsure why