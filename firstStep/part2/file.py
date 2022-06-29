# file = open('phytonEducation/firstStep/part2/static/textFile.txt', 'a')
# file.write('Hello Worlds!\n')
# file.close()

# with open('phytonEducation/firstStep/part2/static/textFile.txt', 'r') as file:
#     print(file.read())


with open('phytonEducation/firstStep/part2/static/dataset_24465_4.txt', 'r') as file:
    rows = file.read().splitlines()
    rows.reverse()

for text in rows:
    # print(text)
    pass

with open('phytonEducation/firstStep/part2/static/datasetAnswer.txt', 'w') as file:
    for text in rows:
        file.write(text + '\n')


with open('phytonEducation/firstStep/part2/static/dataset_24465_4.txt', 'r') as file, open('phytonEducation/firstStep/part2/static/datasetAnswer.txt', 'w') as file2:
    for lines in reversed(file.readlines()):
        file2.write(lines)
        file2.write('\n')