def nearest_value(values: set, one: int) -> int:
    holder = {val: abs(val - one) for val in values}
    # {17: 8, 4: 5, 7: 2, 10: 1, 11: 2, 12: 3}
    mins = min(holder.values())
    # 1
    return min(k for k, v in holder.items() if v == mins)

    return min(values, key=lambda n: (abs(one - n), n))

    if one in values:   
        return one
    values = sorted(values)
    minV = values[0]
    maxV = values[-1]
    for num in values:
        if (num < one) and (num > minV):
            minV = num
        if (num > one) and (num < maxV):
            maxV = num

    result = ''
    currentMax = one
    currentMin = one
    while (True):
        currentMin -= 1
        if (currentMin == minV):
            result = minV
            break

        currentMax += 1
        if (currentMax == maxV):
            result = maxV
            break

    return result


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    # assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    # assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    # assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    # assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    # assert nearest_value({5}, 5) == 5
    # assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")