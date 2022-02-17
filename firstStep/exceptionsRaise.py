from unicodedata import name


class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError()
        super().append(x)

x = PositiveList()
x.append(1)
# таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
#  а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.