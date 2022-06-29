import operator as op
from functools import partial


names = [
    ('Haskell', 'Curry'),
    ('Guido', 'van', 'Rossum'),
    ('John', 'Backus'),
]

sortByLast = partial(list.sort, key=op.itemgetter(-1))
print(names)
sortByLast(names)
print(names)

letters = ['dfe','cba',  'ghi']
sortByLast(letters)
print(letters)