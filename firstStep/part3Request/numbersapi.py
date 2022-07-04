import requests

urlPattern = 'http://numbersapi.com/{}/math?json=true'
with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\dataset_24476_3.txt') as file:
    for line in file:
        num = line.strip()
        if not num:
            continue
        url = urlPattern.format(num)
        response = requests.get(url).json()
        if response['found']:
            print('Interesting')
        else:
            print('Boring')
    
