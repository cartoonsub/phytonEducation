
def getBiggestNumber(numbers: list) -> int:
    array = insertion_sort(numbers)
    return int(''.join(array))


def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i

        while j > 0 and compareTwoNumbers(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert

    return array


def compareTwoNumbers(a: str, b: str) -> int:
    if (int(a) == int(b)):
        return 0
    
    if a[0] > b[0]:
        return 1

    if a[0] < b[0]:
        return 0

    maximum = max(len(a), len(b))
    last_a = 0
    last_b = 0

    for i in range(maximum):
        if (len(a)) > i:
            last_a = int(a[i])

        if (len(b)) > i:
            last_b = int(b[i])
            
        if last_a > last_b:
            return 1
        
        if last_a < last_b:
            return 0
    
    return 0


lenght = int(input())
input = input()

numbers = list(map(str, input.split()))
print(getBiggestNumber(numbers))
