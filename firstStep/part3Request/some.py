def backward_string(val: str) -> str:
    text = list(val)
    text.reverse()
    print(val[::-1])
    return ('').join(text)

backward_string=lambda s:s[::-1]

if __name__ == '__main__':
    print("Example:")
    print(backward_string('123456789'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string('val') == 'lav'
    # assert backward_string('') == ''
    # assert backward_string('ohho') == 'ohho'
    # assert backward_string('123456789') == '987654321'
    # print("Coding complete? Click 'Check' to earn cool rewards!")

from typing import Iterable

def replace_first(items: list) -> Iterable:
    if not items:
        return []
    items.append(items[0])
    return items[1:]
    if items:
        items.append(items.pop(0))
    return items
    replace_first = lambda items: items[1:]+items[0:1]


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))
    print(list(replace_first([])))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    # assert list(replace_first([1])) == [1]
    # assert list(replace_first([])) == []
    # print("Coding complete? Click 'Check' to earn cool rewards!")
