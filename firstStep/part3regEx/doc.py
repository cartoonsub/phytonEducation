from random import random


string = 'abcdefgc'

print(string.find('c'))

print(string.index('c'))

print(string.startswith('a'))
print(string.startswith(('ab', 'cd')))

print(string.endswith('g'))

print()

print(string.count('c'))

print(string.find('c'))
print(string.rfind('c'))

print('\n')

string = 'The man in black fled across the desert, and th,e gunslinge,r followed'

print(string.lower())
print(string.upper())
print(string.count('the'))
print(string.lower().count('the'))

print('\n')

print(string.replace(',', ', ', 2))

print('\n')

print(string.split(' ', 5))

print('\n')

string = '       The man in black fled across the desert, and the gunslinger followed                    '

print(string.strip())
print(string.strip('The '))
print(string.lstrip())
print(string.rstrip())

print('\n')

print('=>'.join(['1', '2']))
print(repr('=>'.join(['1', '2'])))

number = map(str, range(10))
print('=>'.join(number))

print('\n')

capital = 'London is the capital of Great Britain'
template = '{1} is the capital of {0}'
template = '{} is the capital of {}'
template = '{city} is the capital of {country}'
# print(template.format('London', 'great britain'))
print(template.format(city='vaduz', country='switzerland'))

x = random()
print('{:.2f}'.format(x))