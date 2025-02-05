

# "and"
andCost = len('and')
# 0, 1, 2, ..., 19
smallCosts = list(map(len, ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']))
smallCosts.insert(0,0)
# 0, 10, 20, ..., 90
mediumCosts = list(map(len, ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']))
mediumCosts.insert(0,0)
# 0, 100, 200, ..., 900
bigCosts =  list(map(len, ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']))
bigCosts.insert(0,0)

totalLength = len('onethousand')

for threeDig in range(1, 1000):
    length = 0
    oneDig = threeDig%10
    twoDig = threeDig%100
    if twoDig < 20: # add length of tens and units if < 20
        length += smallCosts[twoDig]
    else: # add length of tens and units if >= 20
        length += smallCosts[oneDig] + mediumCosts[twoDig//10]
    if 100 <= threeDig: # add length of hundreds (and thousand)
        length += bigCosts[threeDig//100]
        if twoDig != 0: # add and if not ending in zero zero
            length += andCost
    totalLength += length

print(totalLength)