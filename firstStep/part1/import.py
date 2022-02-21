# from math import pi 
# r = float(input())
# p = 2 * pi * r
# print(p)

# from sys import argv 
# print(*argv[1:], end=' ')

# import requests
# answer = requests.get('http://webandtravel.ru/')
# print(answer.text)

fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
fib(31)
print(fib(31))