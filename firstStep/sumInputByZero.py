sumNums = int(input())
listNums = [sumNums]
while True:
    if sumNums == 0:
        break
    num = int(input())
    sumNums += num
    listNums += [num]
sumSquare = 0
if len(listNums) > 1:
    for x in listNums:
        sumSquare += x * x
    print(sumSquare)
else: print(listNums[0] * listNums[0])
