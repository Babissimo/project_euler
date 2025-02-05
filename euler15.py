numOfPathsFromPoint = [[1] * 21] * 21

for row in range(1,21):
    for col in range(1,21):
        numOfPathsFromPoint[row][col] = numOfPathsFromPoint[row][col-1] + numOfPathsFromPoint[row-1][col]

print(numOfPathsFromPoint[20][20])


