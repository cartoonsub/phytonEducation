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

    def pop(self):
        if self.is_empty():
            return None
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
    # input = ['peek', 'push 5', 'push 2', 'peek', 'size', 'size', 'push 1', 'size']
    # input = ['push 1', 'size', 'push 3', 'size', 'push 1', 'pop', 'push 1', 'pop', 'push 3', 'push 3']
    # input_quantity = 10
    # size = 1
    input_quantity = int(input())
    size = int(input())
    
    stack = MyQueue(size)

    for i in range(input_quantity):
        # line = str(input())
        # line = input[i]
        line = sys.stdin.readline().rstrip()
        if line == 'peek':
            print(stack.peek())
        elif line == 'size':
            print(stack.size)
        elif line == 'pop':
            print(stack.pop())
        else:
            stack.push(int(line.split()[1]))


if __name__ == '__main__':
    main()
    pass
