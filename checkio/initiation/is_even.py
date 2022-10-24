def is_even(num: int) -> bool:
    print (not(num & 1))
    if num % 2 == 0:
        return True
    return False

print('Example:')
print(is_even(2))

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")