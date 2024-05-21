
gamers = 2
# limit = int(input()) * gamers
numbers = []
# for i in range(4):
#     for number in str(input()):
#         if number.isnumeric():
#             numbers.append(number)

limit = 3 * gamers
texts = ['1231', '2..2', '2..2', '2..2', '44']
for text in texts:
    for number in text:
        if number.isnumeric():
            numbers.append(number)
print(numbers)

total = {}
for number in numbers:
    if number not in total:
        total[number] = 1
    else:
        total[number] += 1

score = {}
print(total)
for number, quantity in total.items():
    print(number, quantity)
print(score)
# 3
# 1231
# 2..2
# 2..2
# 2..2


result = []

print(' '.join(map(str, result)))