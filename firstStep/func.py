def modify_list(l):
    for index in reversed(range(len(l))):
        if l[index] % 2 != 0:
            del l[index]
    for index in range(len(l)):
        l[index] = int(l[index] / 2)


lst =  [1, 3, 5, 7, 8]
print(lst)
modify_list(lst)
print(lst)