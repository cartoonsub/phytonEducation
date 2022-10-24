from unittest import result


def checkio(data: list) -> list:
    return [x for x in data if data.count(x)>1]
    temp = set()
    uniqs = []
    for v in data:
        if v in temp and v in uniqs:
            uniqs.remove(v)
            continue
        if v in temp:
            continue
        uniqs.append(v)
        temp.add(v)
    
    result = []
    for v in data:
        if v in uniqs:
            continue
        result.append(v)
    return result

print('Example:')
print(checkio([5, 5, 5, 5, 5]))

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
assert checkio([10, 20, 30, 10]) == [10, 10]
assert checkio([7]) == []
assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
assert checkio([99, 98, 99]) == [99, 99]
assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")