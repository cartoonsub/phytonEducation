
class MoneyBox:
    def __init__(self, capacity):
        self.total = 0
        self.capacityBox = capacity

    def can_add(self, v):
        if (v == 0):
            return True
        if ((self.total + v) <= self.capacityBox):
            return True
        return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if (self.can_add(v)):
            self.total += v
            return True
        return False

x = MoneyBox(10)
# x.add(5)
# x.add(5)
print(x.add(5))
print(x.add(5))
print(x.add(1))