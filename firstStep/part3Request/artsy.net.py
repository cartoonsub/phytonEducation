
import requests
import json

client_id = '17dc2c2d7961c834e720'
client_secret = 'ad20a843d8b220eaa5d5260a69fd4ed7'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MmMyZjU1ZWQzMTE5NTA1MzlmNGExODIiLCJleHAiOjE2NTc1NDg4MzIsImlhdCI6MTY1Njk0NDAzMiwiYXVkIjoiNjJjMmY1NWVkMzExOTUwNTM5ZjRhMTgyIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYyYzJmNWEwZmFhNDI4MGI1YzEwYzhkMSJ9.z-coYf1PkUBp6SmWUzRd01A2OjLyDWB1wF-GMS_HFfs'

# # инициируем запрос на получение токена
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })

# # разбираем ответ сервера
# j = json.loads(r.text)

# # достаем токен
# token = j["token"]
# print(token)
# print(j)

arts = {}
with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\dataset_24476_4.txt') as file:
    for line in file:
        id = line.strip()
        if not id:
            continue
        # создаем заголовок, содержащий наш токен
        headers = {"X-Xapp-Token" : token}
        # инициируем запрос с заголовком
        result = requests.get("https://api.artsy.net/api/artists/{}".format(id), headers=headers).json()
        name = result['sortable_name']
        birthDay = result['birthday']
        arts[name] = birthDay


def sortDict(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)

    for w in sorted_keys:
        sorted_dict[w] = dict[w]
    return sorted_dict


listArtist = (sorted(arts.items(), key=lambda x: (x[1], x[0])))
for artist in listArtist:
    print(artist[0].strip())
# print(sorted(arts.items(), key=lambda x: (x[1], x[0])))
