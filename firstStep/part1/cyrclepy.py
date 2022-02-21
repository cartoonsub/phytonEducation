num = int(input())
if (num == 0 or num == 1):
    print(num)
    exit()
array = [[0] * (num*2) for i in range(num*2)]
posX = (num*2 // 2)
posY = (num*2 // 2)
array[posX][posY] = num**2
arrayNums = [x for x in reversed(range(1, (num**2)))]
lenArrayNum = len(array)
posNum = 0
if num % 2 == 0:
    for count in range(1, len(array)+1):
        for counter in range(count):
            if (count % 2 == 0):
                posY += -1
                posX += 0
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
            else:
                posY += 1
                posX += 0
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
        for counter in range(count):
            if (count % 2 == 0):
                posY += 0
                posX += 1
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
            else:
                if (count != len(array)):
                    posY += 0
                    posX += -1
                    if (posX == -1 or posY == -1):
                        break
                    if posNum == len(arrayNums):
                        break
                    array[posX][posY] = arrayNums[posNum]
                    posNum += 1
else:
    for count in range(1, len(array)+1):
        for counter in range(count):
            if (count % 2 == 0):
                posY += 1
                posX += 0
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
            else:
                posY += -1
                posX += 0
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
        for counter in range(count):
            if (count % 2 == 0):
                posY += 0
                posX += -1
                if (posX == -1 or posY == -1):
                    break
                if posNum == len(arrayNums):
                    break
                array[posX][posY] = arrayNums[posNum]
                posNum += 1
            else:
                if (count != len(array)):
                    posY += 0
                    posX += 1
                    if (posX == -1 or posY == -1):
                        break
                    if posNum == len(arrayNums):
                        break
                    array[posX][posY] = arrayNums[posNum]
                    posNum += 1

for i in range(len(array)):
    for j in range(len(array[i])):
        if (array[i][j] == 0):
            continue
        print(array[i][j], end=' ')
    print()