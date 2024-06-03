
# https://contest.yandex.ru/contest/22781/run-report/114902164/

'''
-- ПРИНЦИП РАБОТЫ --
Класс Deck реализует структуру данных "очередь" 
с операциями добавления и удаления элементов с обоих концов. 
Очередь реализована как кольцевой буфер, что позволяет эффективно добавлять и удалять элементы 
без необходимости перемещения остальных элементов.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Алгоритм корректен, потому что он правильно обрабатывает все возможные случаи. 
Если очередь полна, операции push_front и push_back выводят ошибку и не добавляют элемент. 
Если очередь пуста, операции pop_front и pop_back выводят ошибку и не удаляют элемент. 
Во всех остальных случаях операции выполняются корректно.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность всех операций константна, O(1), 
потому что каждая операция выполняет фиксированное количество действий, не зависящее от размера очереди.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность алгоритма равна O(n), где n - максимальный размер очереди. 
Это объясняется тем, что очередь хранит максимум n элементов.
'''

class Deck:
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
            self.pointer[0] = 0
            return
        
        value = self.queue[self.pointer[0]]
        print(value)
        self.queue[self.pointer[0]] = None
        self.pointer[0] = (self.pointer[0] - 1) % self.size
        self.current_size -= 1
        if self.current_size == 0:
            self.pointer = [None, None]
    
    def pop_back(self):
        if self.pointer[1] is None:
            print('error')
            return
        
        if self.queue[self.pointer[1]] is None:
            print('error')
            self.pointer[1] = 0
            return
        
        value = self.queue[self.pointer[1]]
        print(value)
        self.queue[self.pointer[1]] = None
        self.pointer[1] = (self.pointer[1] + 1) % self.size
        self.current_size -= 1
        if self.current_size == 0:
            self.pointer = [None, None]

    def peek(self):
        return self.queue


def main():
    input_quantity = int(input())
    deck_size = int(input())

    deck = Deck(deck_size)

    for i in range(input_quantity):
        line = input()
        if line == 'pop_front':
            deck.pop_front()
        elif line == 'pop_back':
            deck.pop_back()
        elif 'push_back' in line:
            deck.push_back(int(line.split()[-1]))
        elif 'push_front' in line:
            deck.push_front(int(line.split()[-1]))


if __name__ == '__main__':
    main()
