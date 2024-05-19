result = ''
number = int(input())
if number == 0:
    result = '0'



while (number / 2 > 0):
    symbol = str(number % 2)
    number = int(number / 2)
    result = symbol + result

print(result)