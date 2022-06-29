
def even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some = (map(lambda x: x + 1, nums))
some = map(int, nums)
some = map(even, nums)

evens = filter(even, nums)
print(list(some))
print(list(evens))

evens = filter(even, nums)
for i in evens:
    print(i)


evens = lambda x: x % 2 == 0
print(list(map(evens, nums)))

print(list(filter(evens, nums)))
print('\n\n')

def lenght(name):
    return len(" ".join(name))

names = [
    ('Haskell', 'Curry'),
    ('Guido', 'van', 'Rossum'),
    ('John', 'Backus'),
]

nameLenght = [lenght(name) for name in names]
print(nameLenght)
names.sort(key=lenght)
print(names)
print('\n\n')

names.sort(key=lambda name: len(' '.join(name)), reverse=True)
print(names)


print('\n\n')

import operator as op

f = op.itemgetter(-1)
names.sort(key=f)

print(names)

print('\n\n')