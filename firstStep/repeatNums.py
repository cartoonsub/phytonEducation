nums = [i for i in range(1, int(input())+1)]
allNum = []
for i in nums:
    for x in range(i):
        allNum += [i]
    print(allNum[i-1], end=' ')