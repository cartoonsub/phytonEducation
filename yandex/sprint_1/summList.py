
lenght = int(input())
numberOne = str(input()).replace(' ', '')
numberTwo = str(input()).replace(' ', '')

# numberOne = '95'
# numberTwo = '17'
numberOneLenght = len(numberOne)
numberTwoLenght = len(numberTwo)
longest = max(numberOneLenght, numberTwoLenght)

numberOne = numberOne.rjust(longest, '0')
numberTwo = numberTwo.rjust(longest, '0')

numberOne = numberOne[::-1]
numberTwo = numberTwo[::-1]

numberOne = list(map(int, numberOne))
numberTwo = list(map(int, numberTwo))

result = []
remains = 0
for index in range(longest):
    digitOne = int(numberOne[index])
    digitTwo = int(numberTwo[index])
    sum = digitOne + digitTwo + remains
    
    value = sum % 10
    remains = sum // 10
    # numberOne[index] = str(value)
    result.append(value)

if remains > 0:
    result.append(remains)

result = result[::-1]
print(' '.join(map(str, result)))




