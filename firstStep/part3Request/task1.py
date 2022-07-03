
import requests
import re

link = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
needLink = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

# link = input()
# needLink = input()

def getAllLinks(text):
    links = re.findall(r'<a href="(.*?)">', text)
    return links

def findNeedLink(link, needLink, level = 0, previousLink = ''):
    if level > 1 and link == needLink:
        return True
    level += 1
    if level > 2:
        return False
    if previousLink == link:
        return False

    result = requests.get(link)
    if (result.status_code) != 200:
        return False
    text = format(result.content)
    # text = result.text
    links = getAllLinks(text)
    for newLink in links:
        answer = findNeedLink(newLink, needLink, level, link)
        if answer:
            return True

if findNeedLink(link, needLink):
    print('Yes')
else:
    print('No')