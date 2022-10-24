
def checkio(array: list[int]) -> int:
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]
    if not array:
        return 0
    numbers = {}
    for i in range(len(array)):
        numbers[i] = array[i]

    sumNumbs = sum(int(word) for index, word in numbers.items() if not(index & 1))
    
    return (sumNumbs * array[-1])


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
