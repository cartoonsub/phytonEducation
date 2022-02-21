data = {}
data['clubs'] = {}
data['games'] = int(input())
for numInput in range(data['games']):
    score = input().split(';')
    club1 = score[0]
    club2 = score[2]
    club1Gls = int(score[1])
    club2Gls = int(score[3])

    if club1 not in data['clubs']:
        data['clubs'][club1] = {}
        data['clubs'][club1]['games'] = 0
        data['clubs'][club1]['win'] = 0
        data['clubs'][club1]['pare'] = 0
        data['clubs'][club1]['lose'] = 0
        data['clubs'][club1]['count'] = 0
    if club2 not in data['clubs']:
        data['clubs'][club2] = {}
        data['clubs'][club2]['games'] = 0
        data['clubs'][club2]['win'] = 0
        data['clubs'][club2]['lose'] = 0
        data['clubs'][club2]['pare'] = 0
        data['clubs'][club2]['count'] = 0

    data['clubs'][club1]['games'] += 1
    data['clubs'][club2]['games'] += 1
    if club1Gls > club2Gls:
        data['clubs'][club1]['win'] += 1
        data['clubs'][club2]['lose'] += 1
        data['clubs'][club1]['count'] += 3
    elif club1Gls == club2Gls:
        data['clubs'][club2]['pare'] += 1
        data['clubs'][club1]['pare'] += 1
        data['clubs'][club2]['count'] += 1
        data['clubs'][club1]['count'] += 1
    else:
        data['clubs'][club2]['win'] += 1
        data['clubs'][club1]['lose'] += 1
        data['clubs'][club2]['count'] += 3

for club, dataClub in data['clubs'].items():
    print(club + ':', end='')
    print(dataClub['games'], end=' ')
    print(dataClub['win'], end=' ')
    print(dataClub['pare'], end=' ')
    print(dataClub['lose'], end=' ')
    print(dataClub['count'], end=' ')
    print()