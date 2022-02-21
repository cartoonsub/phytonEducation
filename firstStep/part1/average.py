# a, b = (int(i) for i in input().split())
a = int(input())
b = int(input())
count = 0
countNums = 0
for num in range(a, b +1):
    if num % 3 == 0:
        countNums += 1
        count += num
if countNums != 0:
    print(count / countNums)

a = int(input())
b = int(input())
a += -a%3
b -= b%3
print((a+b)/2)