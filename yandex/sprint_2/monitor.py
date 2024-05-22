

rows = int(input())
columns = int(input())

matrix = {}
for i in range(rows):
    matrix[i] = input().split(' ')

# rows = 4
# columns = 3
# matrix = {0: ['1', '2', '3'], 1: ['0', '2', '6'], 2: ['7', '4', '1'], 3: ['2', '7', '0']}

result = []
for i in range(columns):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    # result.append(row)
    print(' '.join(map(str, row)))

# print(' '.join(map(str, result)))