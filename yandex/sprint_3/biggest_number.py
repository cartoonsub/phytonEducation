
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
    firstNumber = int(''.join(a + b))
    secondNumber = int(''.join(b + a))
    if firstNumber > secondNumber:
        return 1

    return 0


lenght = int(input())
input = input()
numbers = list(map(str, input.split()))
print(getBiggestNumber(numbers))




