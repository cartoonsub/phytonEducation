
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

uniq = []
ans = 0
for obj in objects: # доступная переменная objects
    if obj in uniq:
        continue
    uniq.append(obj)
    ans += 1
    
print(ans)
