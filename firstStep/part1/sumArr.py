ar = [int(i) for i in '1 3 5 6 10'.split()]
for i in range(len(ar)):
    print(ar[i-1] + ar[i+1-len(ar)], end= ' ')
sumNum = ''
count = 0
arLen = len(ar) - 1

for num in ar:
    if (arLen == 0):
        sumNum = num;
        break
    if count == 0:
        sumNum += str(ar[arLen] + ar[count+1]) + ' '
        count += 1
        continue
    if count == arLen:
        sumNum += str(ar[count - 1] + ar[0])
        break
    sumNum += str(ar[count - 1] + ar[count + 1]) + ' '
    count += 1
# print(sumNum)
