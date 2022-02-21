# put your python code here
import sys
sys.stdin = open("phytonEducation/firstStep\static/test.txt", "r")

n = int(input())
sl = {}
def func(x):
    if len(x) == 1:
        return [x[0], []]
    return [x[0], x[1].split()]

for _ in range(n):
    m = input().split(' : ')
    sl[func(m)[0]] = func(m)[1]
             
def func1(x, sl):
    sp = [x]
    for key, value in sl.items():
        if x in value:
            sp.append(key)
            sp.extend(func1(key, sl))
    return sp        
        

for _ in range(int(input())):
    x, y = input().split()
    if y in func1(x, sl):
        print('Yes')
    else: print('No')
        
               