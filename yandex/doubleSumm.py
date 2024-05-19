
# numberOne = '1'
# numberTwo = '1'

numberOne = str(input())
numberTwo = str(input())


numberOneLenght = len(numberOne)
numberTwoLenght = len(numberTwo)
longest = max(numberOneLenght, numberTwoLenght)

numberOne = numberOne.ljust(longest, '0')
numberTwo = numberTwo.ljust(longest, '0')

numberOne = numberOne[::-1]
numberTwo = numberTwo[::-1]

result = ''
remains = 0
for index in range(longest):
    digitOne = int(numberOne[index])
    digitTwo = int(numberTwo[index])
    sum = digitOne + digitTwo + remains
    value = sum % 2
    remains = sum // 2
    result = str(value) + result

if remains > 0:
    result = str(remains) + result

print(result)