
from random import random

books = {
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'The Catcher in the Rye': 'J. D. Salinger',
    'To Kill a Mockingbird': 'Harper Lee',
}

iterator = iter(books)
print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
    def __iter__(self):
        return self

x = RandomIterator(3)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

print("\n")
for x in RandomIterator(10):
    print(x)