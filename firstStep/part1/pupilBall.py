

dataFromFile = {}
with open('dataset_3363_4.txt', 'r') as file:
    for line in file:
        lineData = line.strip().split(';')
        # print(lineData[1:])
        dataFromFile[lineData[0]] = lineData[1:]

middleMarks = {}
for name, listMark in dataFromFile.items():
    middle = 0
    for index in range(len(listMark)):
        if index in middleMarks:
            middleMarks[index] += [int(listMark[index])]
        else:
            middleMarks[index] = [int(listMark[index])]
        middle += int(listMark[index])
    print(middle/len(listMark), end=' ')
    print()
    
for index, marks in middleMarks.items():
    summ = 0
    for num in marks:
        summ += num
    print(summ / len(marks), end=' ')

