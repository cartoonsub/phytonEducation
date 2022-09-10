from re import T
from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # return [ch1+ch2 for ch1,ch2 in zip(text[::2],text[1::2]+'_')]
    
    # split_pairs = lambda a: [i + k for i, k in zip(a[::2], a[1::2] + '_')]

    # text += '_' if len(text) % 2 else ''
    # return [text[i:i + 2] for i in range(0, len(text), 2)]


    result = []
    if not text:
        return result

    count = len(text)
    text = list(text)
    isOdd = False
    
    if count % 2 > 0:
        isOdd = True
    while text:
        part = ("".join(text[0:2]))
        text.pop(0)
        if not text and isOdd:
            part += '_'
        result.append(part)
        if not text:
            continue
        text.pop(0)
    
    return result


print("Example:")
print(list(split_pairs("abcde")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
