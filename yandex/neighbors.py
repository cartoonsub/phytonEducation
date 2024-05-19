lenght = int(input())
columnsLenght = int(input())

matrix = []
for i in range(lenght):
    matrix.append(input().split())

row = int(input())
column = int(input())

rowsForSearch = {
    row: [column - 1, column + 1]
}

if (row + 1) < lenght:
    rowsForSearch[row + 1] = [column]
if (row - 1) >= 0:
    rowsForSearch[row - 1] = [column]


result = []
for rowIndex, columns in rowsForSearch.items():
    if not matrix[rowIndex]:
        continue
    for column in columns:
        if column < 0:
            continue
        if column >= columnsLenght:
            continue
        value = int(matrix[rowIndex][column])
        result.append(value)

result.sort()
print(' '.join(map(str, result)))







