

def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    # your code here
    frequently = {}
    for string in data:
        if (string in frequently):
            frequently[string] += 1
            continue
        frequently[string] = 1
    
    maxValue = 0
    result = ''
    for key, value in frequently.items():
        if value > maxValue:
            maxValue = value
            result = key
    return result
    
# from statistics import mode as most_frequent
# def most_frequent(data):
#     return max(set(data), key=data.count)

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
