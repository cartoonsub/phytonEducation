array = [int(i) for i in input().split()]
need = int(input())
count = 0
for num in range(len(array)):
    if need == array[num]:
        print(num, end=' ')
        count += 1
if count == 0:
    print('Отсутствует')