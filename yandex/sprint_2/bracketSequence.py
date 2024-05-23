import sys


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_value = []

    def push(self, item):
        self.items.append(item)
        if not self.max_value or item >= self.max_value[-1]:
            self.max_value.append(item)

    def pop(self):
        if not self.items:
            print('error')
            return
    
        if self.items.pop() == self.max_value[-1]:
            self.max_value.pop()

    def get_max(self):
        if not self.max_value:
            return None
        return self.max_value[-1]

    def top(self):
        if not self.items:
            return 'error'
        return self.items[-1]


def main():
    stack = StackMaxEffective()

    input_quantity = int(input())
    for i in range(input_quantity):
        # line = str(input())
        line = sys.stdin.readline().rstrip()
        if line == 'get_max':
            print(stack.get_max())
        elif line == 'pop':
            stack.pop()
        elif line == 'top':
            print(stack.top())
        else :
            stack.push(int(line.split()[1]))


if __name__ == '__main__':
    main()
