# https://contest.yandex.ru/contest/22450/run-report/114417990/

gamers = 2
limit = int(input()) * gamers
numbers = []
for i in range(4):
    for number in str(input()):
        if number.isnumeric():
            numbers.append(number)


total = {}
for number in numbers:
    if number in total:
        total[number] += 1
    else:
        total[number] = 1

score = {}
for number, quantity in total.items():
    if quantity in score:
        score[quantity] += 1
    else:
        score[quantity] = 1

result = 0
for number, quantity in score.items():
    if number > limit:
        continue
    result += quantity

print(result)

def main():
    pass

if __name__ == '__main__':
    main()
