
sum = 0

is_composite = [0] * 2000001

index = 2

while index < 2000000:
    if is_composite[index] == 0:
        sum += index
        for multiple in range(2*index, 2000000, index):
            is_composite[multiple] = 1
    index += 1

print(sum)