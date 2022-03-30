from datetime import datetime
import time


def binary_search(list, item):
    print('search')
    low = 0
    high = len(list)-1
    num = 0
    while low <= high:
        num += 1
        mid = (low + high) // 2
        print('mid: ', mid)
        gues = list[mid]
        if gues == item:
            print('количество:', num)
            return mid
        if gues > item:
            high = mid -1
        else:
            low = mid + 1
    return None

myList = []
for i in range(1, 100):
    myList.append(i)


start_time = datetime.now()
print('answer: ',binary_search(myList, 99))

print(datetime.now() - start_time)