
# https://contest.yandex.ru/contest/22781/run-report/114902164/

'''
-- ПРИНЦИП РАБОТЫ --
Класс Deckue реализует структуру данных "очередь" 
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
Это объясняется тем, что очередь хранит максимум m элементов.
'''

class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.pointer = [None, None]
        self.size = m
        self.current_size = 0

    def push_front(self, value):
        if self.current_size >= self.size:
            raise IndexError

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
            raise IndexError

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
            raise IndexError
        
        if self.queue[self.pointer[0]] is None:
            self.pointer[0] = 0
            raise ValueError
        
        value = self.queue[self.pointer[0]]
        self.queue[self.pointer[0]] = None
        self.pointer[0] = (self.pointer[0] - 1) % self.size
        self.current_size -= 1
        if self.current_size == 0:
            self.pointer = [None, None]

        return value
    
    def pop_back(self):
        if self.pointer[1] is None:
            raise IndexError
        
        if self.queue[self.pointer[1]] is None:
            self.pointer[1] = 0
            raise ValueError
        
        value = self.queue[self.pointer[1]]
        self.queue[self.pointer[1]] = None
        self.pointer[1] = (self.pointer[1] + 1) % self.size
        self.current_size -= 1
        if self.current_size == 0:
            self.pointer = [None, None]
        
        return value

    def peek(self):
        return self.queue


def main():
    input_quantity = int(input())
    deque_size = int(input())
    deckue = Deque(deque_size)

    for i in range(input_quantity):
        try: 
            line = input()
            if line == 'pop_front':
                print(deckue.pop_front())
            elif line == 'pop_back':
                print(deckue.pop_back())
            elif 'push_back' in line:
                deckue.push_back(int(line.split()[-1]))
            elif 'push_front' in line:
                deckue.push_front(int(line.split()[-1]))
        except IndexError:
            print('error') 


if __name__ == '__main__':
    main()
