import sys
sys.stdin = open("phytonEducation/firstStep/part1/static/testNames.txt", "r")

def create(nameSpace, parent):
    if parent == 'global':
        if nameSpace in globals['spaces']:
            globals['spaces'][nameSpace]['parents'].append(parent)
            return
        globals['spaces'][nameSpace] = {'vars':[], 'parents': ['global']}
        return
    if nameSpace in globals['spaces']:
        globals['spaces'][nameSpace]['parents'].append(parent)
        return
    globals['spaces'][nameSpace] = {'vars':[], 'parents': [parent]}

def add(nameSpace, variable):
    if nameSpace == 'global':
        globals['vars'].append(variable)
        return
    
    if nameSpace not in globals['spaces']: #delete this?
        globals['spaces'][nameSpace] = {'vars':[variable], 'parents': []}
        return
    globals['spaces'][nameSpace]['vars'].append(variable)

def get(nameSpace, variable):
    if nameSpace == 'global':
        if variable in globals['vars']:
            return 'global'
        return 'None'
    if nameSpace not in globals['spaces']:
        if variable in globals['vars']:
            return 'global'
        return 'None'
    if variable in globals['spaces'][nameSpace]['vars']:
        return nameSpace
    for parent in globals['spaces'][nameSpace]['parents']:
        result = get(parent, variable)
        if result != 'None':
            return result
        
globals = {
    'vars': [],
    'spaces': {},
}
for i in range(int(input())):
    function, command1, command2 = input().split()
    if function == 'create':
        create(command1, command2)
    if function == 'add':
        add(command1, command2)
    if function == 'get':
        result = get(command1, command2)
        print(result)

# alternative solution:
actions = {
    'create': create,
    'add': add,
    'get': get,
}
for i in range(int(input())):
    function, command1, command2 = input().split()
    actions[function](command1, command2)

# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b
# add foo FUCK
# get global FUCK

# global
# None
# bar
# foo