import sys

# Всё фигня
# нет лимита на добавление элементов
# подумать как сделать правильный кольцевой буфер

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.front_index = 0
        self.back_index = n - 1

    def push_front(self, value):
        if self.queue[self.front_index] is not None:
            print('error')
            return

        self.queue[self.front_index] = value
        self.front_index = (self.front_index + 1)

    def push_back(self, value):
        if self.queue[self.back_index] is not None:
            print('error')
            return
        
        self.queue[self.back_index] = value
        self.back_index = (self.back_index - 1)


    def pop_front(self):
        if self.queue[self.front_index] is None:
            print('error')
            return
        
        value = self.queue[self.front_index]
        print(value)
        self.queue[self.front_index] = None
        # if self.is_empty():
        #     print('error')
        #     return None
        # x = self.queue[self.head]
        # self.queue[self.head] = None
        # self.head = (self.head + 1) % self.max_n
        # self.size -= 1
        # return x
    
    def pop_back(self):
        if self.queue[self.back_index] is None:
            print('error')
            return
        
        value = self.queue[self.back_index]
        print(value)
        self.queue[self.back_index] = None


    def peek(self):
        return self.queue


def main():
    input_quantity = 7
    deck_size = 10
    input = [
        'push_front -855',
        'push_front 0',
        'pop_back',
        'pop_back',
        'push_back 844',
        'pop_back',
        'push_back 823'
    ]

    # input_quantity = 4
    # deck_size = 4
    # input = [
    #     'push_front 861',
    #     'push_front -819',
    #     'pop_back',
    #     'pop_back',
    # ]

    input_quantity = 6
    deck_size = 6
    input = [
        'push_front -201',
        'push_back 959',
        'push_back 102',
        'push_front 20',
        'pop_front',
        'pop_back',
    ]
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

    print(Deck.peek())

if __name__ == '__main__':
    main()
