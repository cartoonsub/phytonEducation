def middleCount(counts):
    if not counts:
        return '-'
    summ = 0
    for num in counts:
        summ += int(num)
    return summ / len(counts)

classes = {a: [] for a in range(1, 12)}
with open('dataset_3380_5.txt', 'r') as file:
    for line in file:
        dataLine = line.strip().split('\t')
        key = int(dataLine[0])
        data = classes[key]
        data.append(dataLine[2])
        classes[key] = data

# print(classes)
with open('dateReturn.txt', 'w') as file:
    for key, sizes in classes.items():
        print(key, middleCount(sizes), end='')
        print()
        data = str(key) + ' ' + str(middleCount(sizes)) + '\n'
        file.write(data)