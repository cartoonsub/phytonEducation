
def binarySearch(price, numbers, index_start, index_end, result):
    if index_end == index_start:
        value = numbers[index_start]
        if (value >= price):
            result = index_start
        return result
    
    mid = (index_end + index_start) // 2
    value = numbers[mid]
    if (value >= price):
        result = mid
        index_end = mid - 1
        if index_end < 0:
            index_end = 0
        if numbers[index_end] < price:
            return result
    else:
        index_start = mid + 1
        if index_start > len(numbers) - 1:
            index_start = len(numbers) - 1
    
    result = binarySearch(price, numbers, index_start, index_end, result)
    return result


days = int(input())
numbers = list(map(int, input().split()))
price = int(input())

# import time
# days = 17
# numbers = list(map(int, '12 19 29 31 33 37 52 62 66 68 71 75 75 88 90 93 98'.split()))
# price = 28

index_start, index_end = 0, len(numbers) - 1
result = str(binarySearch(price, numbers, index_start, index_end, -2) + 1) + ' '
result += str(binarySearch(price * 2, numbers, index_start, index_end, -2) + 1)
print(result)
