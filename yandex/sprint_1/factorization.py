import math
number = int(input())
# number = 8
# number = 13
# number = 100
# number = 14

result = ''

multiplier = 2
sqrt = math.sqrt(number)
for i in range(2, int(sqrt) + 1):
    while number % i == 0:
        result += str(i) + ' '
        number = number // i

if number != 1:
    result += str(number) + ' '

if result:
    print(result.strip())


