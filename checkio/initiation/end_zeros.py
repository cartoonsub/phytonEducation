def end_zeros(num: int) -> int:
    total = 0
    listOfNums = list(str(num))
    listOfNums.reverse()
    for x in listOfNums:
        if x == '0':
            total += 1
        else:
            break
    return total


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(100100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")

print('fuck')
print(5 % 2)