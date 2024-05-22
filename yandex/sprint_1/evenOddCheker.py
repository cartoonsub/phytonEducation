# В первой строке записаны три случайных целых числа a, b и c. Числа не превосходят 109 по модулю.

# a, b, c = map(int, input().split())
# input = input().split()
input = '-23 6 24'.split()

result = 0
for i in input:
    if int(i) % 2 == 0:
        result += 1

if result == 3 or result == 0:
    print('WIN')
else:
    print('FAIL')
    