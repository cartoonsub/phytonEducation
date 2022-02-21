coordinates = [input() for _ in range(int(input()))]
result = [0,0]

for direct in coordinates:
    directon = direct.split(' ')
    directon[1] = int(directon[1])
    if directon[0].lower() == 'север':
        result[1] += directon[1]
    if directon[0].lower() == 'юг':
        result[1] -= directon[1]
    if directon[0].lower() == 'запад':
        result[0] -= directon[1]
    if directon[0].lower() == 'восток':
        result[0] += directon[1]
print(*result)