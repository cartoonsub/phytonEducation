# https://contest.yandex.ru/contest/22450/run-report/114402642/

def reverseWalk(result, index, indexEnd):
    start = 0
    while index > indexEnd:
        if indexEnd < 0:
            result[index] = start
            
        if indexEnd >= 0 and result[index] > start:
            result[index] = start

        index -= 1
        start += 1

def main():
    lenght = int(input())
    street = str(input()).split(' ')

    result = []

    currentZeroIndex = None
    previousZeroIndex = None
    start = 1

    for index in range(len(street)):
        value = int(street[index])
        if value == 0:
            result.append(0)
            if previousZeroIndex is None:
                previousZeroIndex = -1
            else:
                previousZeroIndex = currentZeroIndex
            
            currentZeroIndex = index

            reverseWalk(result, currentZeroIndex, previousZeroIndex)
            start = 1
            continue

        result.append(start)
        start += 1

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
