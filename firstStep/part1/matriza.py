array = []
while True:
    inputData = input()
    if inputData == 'end':
        break
    nums = [int(i) for i in inputData.split()]
    array += [nums]
# (i-1, j), (i+1, j), (i, j-1), (i, j+1)
if not array:
    print('fuck')

for i in range(len(array)):
    for j in range(len(array[i])):
        a = array[i-1][j]
        b = array[i-(len(array))+1][j]
        c = array[i][j-1]
        d = array[i][j-(len(array[i]))+1]
        print(a+b+c+d, end = ' ')
    print()