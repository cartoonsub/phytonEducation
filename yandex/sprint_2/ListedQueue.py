import sys

class MyQueue:
    def __init__(self, n):
            self.queue = [None] * n
            self.head = 0
            self.tail = 0
            self.max_n = n
            self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, x):
        if self.size == self.max_n:
            print('error')
            return
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1 

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head];
        self.queue[self.head] = None;
        self.head = (self.head + 1) % self.max_n;
        self.size -= 1;
        return x; 

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def get_max(self):
        if not self.max_value:
            return None
        return self.max_value[-1]

    def top(self):
        if not self.items:
            return 'error'
        return self.items[-1]


def main():
    # # 10
    # input = ['put -34', 'put -23', 'get', 'size', 'get', 'size', 'get', 'get', 'put 80', 'size']
    # # 6
    # input = ['put -66', 'put 98', 'size', 'size', 'get', 'get']
    # # 9
    # input = ['get', 'size', 'put 74', 'get', 'size', 'put 90', 'size', 'size', 'size']
    # input_quantity = 9

    input_quantity = int(input())
    stack = MyQueue(input_quantity)

    for i in range(input_quantity):
        # line = str(input())
        # line = input[i]
        line = sys.stdin.readline().rstrip()
        if line == 'get':
            print(stack.get())
        elif line == 'size':
            print(stack.size)
        else:
            stack.push(int(line.split()[1]))


if __name__ == '__main__':
    main()
    pass
