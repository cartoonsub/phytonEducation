
class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print('error')
            return
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)

    def top(self):
        if not self.items:
            return 'error'
        return self.items[-1]

    def print_stack(self):
        print(self.items)


stack = StackMaxEffective()

inputQuantity = int(input())
for i in range(inputQuantity):
    line = str(input())
    if line == 'get_max':
        print(stack.get_max())
    elif line == 'pop':
        stack.pop()
    elif line == 'top':
        print(stack.top())
    elif line.startswith('push'):
        stack.push(int(line.split()[1]))

# stack.print_stack()
