# https://contest.yandex.ru/contest/22450/run-report/114402642/

def reverse_walk(result, index, index_end):
    start = 0
    while index > index_end:
        if index_end < 0:
            result[index] = start
            
        if index_end >= 0 and result[index] > start:
            result[index] = start

        index -= 1
        start += 1


def main():
    lenght = int(input())
    street = str(input()).split(' ')

    result = []

    current_zero_index = None
    previous_zero_index = None
    start = 1

    for index in range(len(street)):
        value = int(street[index])
        if value == 0:
            result.append(0)
            if previous_zero_index is None:
                previous_zero_index = -1
            else:
                previous_zero_index = current_zero_index
            
            current_zero_index = index

            reverse_walk(result, current_zero_index, previous_zero_index)
            start = 1
            continue

        result.append(start)
        start += 1

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
