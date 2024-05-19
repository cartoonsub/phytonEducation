
row1 = 3
row2 = '1 8 9'
row3 = '2 3 1'

row1 = input()
row2 = input()
row3 = input()

lenght = int(row1)


result = ''
firstNumbers = row2.split()
secondNumbers = row3.split()

for index in range(lenght):
    result += firstNumbers[index] + ' ' + secondNumbers[index] + ' '

print(result.strip())