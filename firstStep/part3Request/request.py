import requests

result = requests.get('https://cartoonsub.com/',
                      params={'q': 'batman'
                              })
print(result.status_code)
print(result.headers['content-type'])
print(result.headers)
# print(result.text)
# print(result.content)

with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part2\\static\\image.html', 'w') as f:
    f.write(result.text)
