import json

src = '[{"name": "DH", "parents": ["D", "BF", "DE", "AE"]}, {"name": "D", "parents": ["AE"]}, {"name": "B", "parents": []}, {"name": "AE", "parents": ["F"]}, {"name": "BG", "parents": ["H", "CH"]}, {"name": "H", "parents": []}, {"name": "E", "parents": ["CG", "B"]}, {"name": "BH", "parents": ["CG"]}, {"name": "CE", "parents": []}, {"name": "CH", "parents": ["E"]}, {"name": "C", "parents": ["CE"]}, {"name": "A", "parents": []}, {"name": "DE", "parents": ["BH"]}, {"name": "F", "parents": []}, {"name": "CG", "parents": ["C", "G"]}, {"name": "G", "parents": []}, {"name": "BF", "parents": ["F"]}]'
# src = input()
data = json.loads(src)
collections = {}
for item in data:
    name = item['name']
    parents = item['parents']
    if name not in collections:
        collections[name] = []
    
    for parent in parents:
        if parent not in collections:
            collections[parent] = [name]
        else:
            collections[parent].append(name)

def sortDict(dict):
    sortedDict = {}
    sorted_keys = sorted(dict.keys())
    for w in sorted_keys:
        sortedDict[w] = dict[w]
    return sortedDict

def findParents(collections, name = '', founded = {}, parent=''):
    if name:
        for item in collections[name]:
            if item not in collections:
                continue
            founded[parent].append(item)
            founded = findParents(collections, item, founded, parent)
        return founded

    for key, items in collections.items():
        founded[key] = [key]
        for item in items:
            if item in collections:
                founded[key].append(item)
                founded = findParents(collections, item, founded, key)

    return founded

nums = {}
for key, items in findParents(collections).items():
    nums[key] = len(set(items))

finishData = sortDict(nums)
for key, items in finishData.items():
    print(key, items, sep=' : ')
    pass