import math

number = int(input())
logarithm = math.log(number, 4)
if logarithm.is_integer():
    print(True)
else:
    print(False)



