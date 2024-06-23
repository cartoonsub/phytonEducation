
def sortBubble(inputArray: list, lenght: int) -> None:
    swap = True
    wasSwap = False
    while swap:
        if lenght == 0:
            break
        swap = False
        for i in (range(lenght)):
            a = inputArray[i]
            b = inputArray[i + 1]
            if a > b:
                swap = True
                wasSwap = True
                inputArray[i] = b
                inputArray[i + 1] = a

        if swap == False:
            break
        else:
            lenght -= 1

        print(' '.join(map(str, inputArray)).strip())
    
    if wasSwap == False:
        print(' '.join(map(str, inputArray)).strip())





def bubble_sort_classic(lst):
    n = len(lst) - 1
    for i in range(n):
        print('step:', i, lst, range(0, n - i))
        for j in range(0, n - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lenght = int(input())
input = input()

inputArray = list(map(int, input.split()))
length = len(inputArray) - 1

sortBubble(inputArray, length)