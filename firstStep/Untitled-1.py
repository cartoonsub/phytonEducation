array = [
    'add global a',
    'create foo global',
    'add foo b',
    'get foo a',
    'get foo c',
    'create bar foo',
    'add bar a',
    'get bar a',
    'get bar b',
    ]

spaces = dict()
def create(space, parentSpace):
    if (parentSpace in spaces):
        spaces[parentSpace][space] = {'values': []}
        return
    isHere = False
    for key in spaces:
        if (isHere == True):
            break
        if (parentSpace in spaces[key]):
            spaces[key][parentSpace][space] = {'values': []}
            isHere = True
            break
    if (isHere == False):
        spaces[parentSpace] = {'values': []}
        spaces[parentSpace][space] = {'values': []}
        return

def add(space, value):
    if (space in spaces):
        spaces[space]['values'].append(value)
        return
    isHere = False
    for key in spaces:
        if (space in spaces[key]):
            spaces[key][space]['values'].append(value)
            isHere = True
        for key2 in spaces[key]:
            if (space in spaces[key][key2]):
                spaces[key][key2][space]['values'].append(value)
                isHere = True
    if (isHere == False):
        spaces[space] = {'values': []}
        spaces[space]['values'].append(value)
def get(space, search):
    needSpace = 'None'
    for key, value in spaces.items():
        if (search in spaces[key]['values']):
            needSpace = key
        if (space in spaces[key]):
            if (search in spaces[key][space]['values']):
                needSpace = space
        for key2, value in spaces[key].items():
            if (search in spaces[key][key2]):
                needSpace = space
    print(needSpace)
    

# for i in array:
#     cmd, namespace, arg = i.split()
#     if (cmd == 'create'):
#         create(namespace, arg)
#     elif (cmd == 'add'):
#         add(namespace, arg)
#     elif (cmd == 'get'):
#         get(namespace, arg)
countInput = int(input())
for i in range(countInput + 1):
    if i == 0:
        continue
    cmd, namespace, arg = input().split()
    if (cmd == 'create'):
        create(namespace, arg)
    elif (cmd == 'add'):
        add(namespace, arg)
    elif (cmd == 'get'):
        get(namespace, arg)

