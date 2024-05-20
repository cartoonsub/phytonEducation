
lenght = int(input())
street = str(input()).split(' ')

# lenght = 5
# street = '0 7 9 4 0 8 20'.split(' ')

result = []
reverseIndexes = []

start = 0
for index in range(len(street)):
    value = int(street[index])
    if value == 0:
        start = 0
        reverseIndexes.append(index)
    else:
        start += 1
    
    result.append(start)

start = 0
lastIndex = len(result) - 1
while lastIndex >= 0:
    value = result[lastIndex]

    if value == 0:
        start = 0
    else:
        start += 1
    if start < value:
        result[lastIndex] = start
        
    lastIndex -= 1

print(' '.join(map(str, result)))