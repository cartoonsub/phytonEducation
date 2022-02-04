import requests

url = ''
with open('dataset_3378_2.txt', 'r') as file:
    for line in file:
        lineData = line.strip()
        # print(lineData[1:])
        url = lineData
if url == '':
    print('Не удалось получить url из файла')
    exit()
answer = requests.get(url)
if answer.text == '':
    print('Не удалось скачать ' + url + ' из файла')
    exit()
fileData = answer.text
with open('temp.txt', 'w') as inf:
    inf.write(fileData)

with open('temp.txt', 'r') as file:
    count = 1
    for line in file:
        # print(line, end='')
        count += 1
print(count)

fileDataList = fileData.splitlines()
print(len(fileDataList))