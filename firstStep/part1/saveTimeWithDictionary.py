def f(num):
    return num * 2

listNums = []
size = int(input())
count = 1
while size >= count:
    count += 1
    listNums += [int(input())]

memory = {}
for num in listNums:
    if num in memory:
        print(memory[num])
    else:
        value = f(num)
        memory[num] = value
        print(value)