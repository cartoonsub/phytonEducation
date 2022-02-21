class ExtendedStack(list):
    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a + b)
        # операция сложения

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)
        # операция вычитания

    def mul(self):
        a = self.pop()
        b = self.pop()
        self.append(a * b)
        # операция умножения

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)
        # операция целочисленного деления

def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0

test()