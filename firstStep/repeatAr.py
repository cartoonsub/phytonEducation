ar = [int(i) for i in input().split()]
ar.sort()
lenAr = len(ar)
result = []
for i in range(lenAr):
    if lenAr > 1:
        if ar[i] == ar[i+1-lenAr]:
            if ar[i] not in result:
                result += [ar[i]]
for num in result:
    print(num, end=' ')