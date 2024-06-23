
def getBiggestNumber(numbers: list) -> int:
    array = insertion_sort(numbers)
    return int(''.join(array))


def insertion_sort(array):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i

    while j > 0 and item_to_insert > getFirstDigit(array[j-1]):
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert

  return array


def getFirstDigit(number: str) -> int:
    return number[0]


lenght = int(input())
input = input()

numbers = list(map(str, input.split()))
print(getBiggestNumber(numbers))

