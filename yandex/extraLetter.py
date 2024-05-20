
stringOne = str(input())
stringTwo = str(input())

# stringOne = 'qkbyv'
# stringTwo = 'kbbqyv'


stringOne = list(stringOne)
stringTwo = list(stringTwo)

stringOne.sort()
stringTwo.sort()

# extraLetter = stringOne ^ stringTwo
# print(extraLetter)
# print(extraLetter.pop())

counter = {}

for letter in stringOne:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for letter in stringTwo:
    if letter in counter:
        counter[letter] -= 1
    else:
        counter[letter] = 1

for letter in counter:
    if counter[letter] != 0:
        print(letter)