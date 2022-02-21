
num = int(input())
array = [[0] * num for i in range(num)]
posX = (num // 2)
posY = (num // 2)
if (num % 2 == 0):
    posX -= -1
    posY -= -1 
print(posX, posY, end='')
print()
array[posX][posY] = num**2
arrayNums = [x for x in reversed(range(0, (num**2)))]
lenArrayNum = len(array)
posNum = 0
print(array)
for count in range(1, len(array)+1):
    for counter in range(count):
        if (count % 2 == 0):
            posY += 1
            posX += 0
            if (posX == -1 or posY == -1):
                break
            array[posX][posY] = arrayNums[posNum]
            posNum += 1
        else:
            posY += -1
            posX += 0
            if (posX == -1 or posY == -1):
                break
            array[posX][posY] = arrayNums[posNum]
            posNum += 1
    for counter in range(count):
        if (count % 2 == 0):
            posY += 0
            posX += -1
            if (posX == -1 or posY == -1):
                break
            array[posX][posY] = arrayNums[posNum]
            posNum += 1
        else:
            if (count != len(array)):
                posY += 0
                posX += 1
                if (posX == -1 or posY == -1):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
    print()