from xml.etree import ElementTree



data = {}

xmlText = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# xmlText = input()


# for child_of_root in tree.iter():
#     print(child_of_root.tag, child_of_root.attrib)

def treeProcessing(tree, lvl, data):
    for child in tree:
        color = child.attrib['color']
        if color in data:
            data[color] += lvl
        else:
            data[color] = lvl
        data = treeProcessing(child, lvl + 1, data)
    return data

tree = ElementTree.fromstring(xmlText)
data[tree.attrib['color']] = 1
data = treeProcessing(tree, 2, data)
print(data['red'], data['green'], data['blue'])
print(*data.values())