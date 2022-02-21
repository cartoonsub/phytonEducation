count = int(input())
first = count // 1000
second = count % 1000
a = first // 100
b = (first // 10) % 10
c = first % 10
e = second // 100
f = (second // 10) % 10
g = second % 10
if (first == 0 and second == 0):
    print('Счастливый')
    exit()
if (a + b + c == e + f+ g):
    print('Счастливый')
else:
    print('Обычный')