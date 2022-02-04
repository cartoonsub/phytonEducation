class Buffer:
    def __init__(self):
        self.nums = []

    def add(self, *a):
        for i in a:
            self.nums.append(i)

        while (len(self.nums) >= 5):
           print(self.getSumm())
           self.nums = self.nums[5:]

        # добавить следующую часть последовательности

    def get_current_part(self):
        return (self.nums)
            
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
    
    def getSumm(self):
        summ = 0
        for x in range(5):
            summ += self.nums[x]
        return summ


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]