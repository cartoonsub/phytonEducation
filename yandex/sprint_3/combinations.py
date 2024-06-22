
def generator(n, result = '', counter_open = 0, counter_close = 0):
    if (n * 2) == counter_open + counter_close:
        print(result)
        return
    
    if counter_open < n:
        generator(n, result + '(', counter_open + 1, counter_close)

    if counter_open > counter_close:
        generator(n, result + ')', counter_open, counter_close + 1)


count = 3
generator(count)
