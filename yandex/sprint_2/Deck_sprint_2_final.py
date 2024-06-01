import sys

# print((8 + 1) % 10)
# exit()

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.pointer = [None, None]
        self.size = n
        self.current_size = 0

    def push_front(self, value):
        if self.current_size >= self.size:
            print('error')
            return

        if self.pointer[0] is None:
            self.pointer[0] = 0
        if self.pointer[1] is None:
            self.pointer[1] = 0
        
        index = self.pointer[0]
        if self.queue[index] is not None:
            index = (index + 1) % self.size

        if self.queue[index] is not None:
            return

        self.queue[index] = value
        self.pointer[0] = index
        self.current_size += 1

    def push_back(self, value):
        if self.current_size >= self.size:
            print('error')
            return

        if self.pointer[1] is None:
            self.pointer[1] = 0
        if self.pointer[0] is None:
            self.pointer[0] = 0
        
        index = self.pointer[1]
        if self.queue[index] is not None:
            index = (index - 1) % self.size

        if self.queue[index] is not None:
            return

        self.queue[index] = value
        self.pointer[1] = index
        self.current_size += 1


    def pop_front(self):
        if self.pointer[0] is None:
            print('error')
            return
        
        if self.queue[self.pointer[0]] is None:
            print('error')
            return
        
        value = self.queue[self.pointer[0]]
        print(value)
        self.queue[self.pointer[0]] = None
        self.pointer[0] = (self.pointer[0] - 1) % self.size
    
    def pop_back(self):
        print('index', self.back_index)
        if self.queue[self.back_index] is None:
            print('error')
            return
        
        value = self.queue[self.back_index]
        print(value)
        self.queue[self.back_index] = None
        self.front_index = (self.back_index + 1)


    def peek(self):
        return self.queue


def main():
    input_quantity = 7
    deck_size = 10
    input = [
        'pssssush_front -855',
        'psssush_front 0',
        'psop_back',
        'psop_back',
        # 'push_back 844',
        # 'pop_back',
        # 'push_back 823'
        '',
        '',
        ''

    ]

    # input_quantity = 4
    # deck_size = 4
    # input = [
    #     'push_front 861',
    #     'push_front -819',
    #     'pop_back',
    #     'pop_back',
    # ]

    # input_quantity = 6
    # deck_size = 6
    # input = [
    #     'push_front -201',
    #     'push_back 959',
    #     'push_back 102',
    #     'push_front 20',
    #     'pop_front',
    #     'pop_back',
    # ]
    # 20
    # 102
    # input_quantity = int(input())
    # deck_size = int(input())

    # pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
    # pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
    Deck = MyQueueSized(deck_size)

    for i in range(input_quantity):
        # line = sys.stdin.readline().rstrip()
        line = input[i]
        if line == 'pop_front':
            Deck.pop_front()
        elif line == 'size':
            print(Deck.size)
        elif line == 'pop_back':
            Deck.pop_back()
        elif 'push_back' in line:
            Deck.push_back(int(line.split()[-1]))
        elif 'push_front' in line:
            Deck.push_front(int(line.split()[-1]))


    Deck.push_front(10)
    Deck.push_back(12)
    Deck.push_back(12)
    Deck.push_front(10)
    Deck.push_back(12)
    Deck.push_back(12)
    Deck.push_back(12)
    Deck.push_front(10)
    Deck.push_back(12)
    Deck.push_front(10)
    Deck.push_front(10)


    Deck.pop_back()

    print(Deck.peek())
    print(Deck.pointer)
if __name__ == '__main__':
    main()
