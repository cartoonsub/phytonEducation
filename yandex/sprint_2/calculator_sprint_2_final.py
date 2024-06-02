import sys


# опишите принцип работы вашего алгоритма;
# обоснуйте, почему он должен работать корректно;
# оцените временную и пространственную сложность алгоритма.
'''
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
'''

class Calculator:
    def __init__(self):
        self.stack = []

    def calculate(self, items):
        stack = []

        for item in items:
            if item.lstrip('-').isdigit():
                stack.append(int(item))
                continue

            b = stack.pop()
            a = stack.pop()
            if item == '+':
                stack.append(a + b)
            elif item == '-':
                stack.append(a - b)
            elif item == '*':
                stack.append(a * b)
            elif item == '/':
                stack.append(a // b)

        return stack.pop()

def main():
    items = sys.stdin.readline().rstrip().split()

    calculator = Calculator()
    print(calculator.calculate(items))


if __name__ == '__main__':
    main()
