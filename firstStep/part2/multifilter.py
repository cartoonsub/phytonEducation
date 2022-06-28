
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos > 0:
            return True
        return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        return False
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(i) == True:
                    pos += 1
                else:
                    neg += 1

            decision = self.judge(pos, neg)
            if decision == True:
                yield i


                
        # возвращает итератор по результирующей последовательности
    # def __next__(self):
    #     if self.index >= len(self.iterable):
    #         raise StopIteration
    #     num = self.iterable[self.index]
    #     self.index += 1
    #     for func in self.funcs:
    #         if func(num) == True:
    #             self.pos += 1
    #         else:
    #             self.neg += 1

    #     decision = self.judge(self.pos, self.neg)
    #     self.pos = 0
    #     self.neg = 0
    #     if decision == True:
    #         return num
    #     return self.__next__()


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
