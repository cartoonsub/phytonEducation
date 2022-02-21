import requests

url = ''
with open('dataset_3378_3.txt', 'r') as file:
    for line in file:
        lineData = line.strip()
        print(lineData)
        url = lineData
if url == '':
    print('Не удалось получить url из файла')
    exit()

while url != '':
    answer = requests.get(url)
    if answer.text == '':
        print('Не удалось скачать ' + url + ' из файла')
        exit()
    if (answer.text[0:2] == 'We'):
        print(answer.text)
        exit()
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + answer.text