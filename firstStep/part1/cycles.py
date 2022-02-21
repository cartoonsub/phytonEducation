a = int(input())
b = int(input())
c = int(input())

maxCount = 0
minCount = 0
midCount = 0
if (a >= b):
    maxCount = a
    minCount = b
elif (a <= b):
    maxCount = b
    minCount = a
# нашел большее и меньшее из первых двух
if (c >= maxCount):
    maxCount = c
    if (a >= b):
        minCount = b
        midCount = a
    else:
        minCount = a
        midCount = b
elif (c <= maxCount):
    if (c >= minCount):
        midCount = c
    else:
        midCount = minCount
        minCount = c
print(maxCount)
print(minCount)
print(midCount)