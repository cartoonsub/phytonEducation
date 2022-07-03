
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    if not re.match(r"^\d+$", line):
        continue
    first, second = 0, 0
    nums = re.findall(r"(\d)", line)
    for i in range(len(nums)):
        if i % 2 == 0:
            first += int(nums[i])
        else:
            second += int(nums[i])
    if (first - second) % 3 == 0:
        print(line)

words = ['0', '10010', '00101', '01001', 'Not a number', '1 1', '0 0']
for word in words:
    if not re.match(r"^\d+$", word):
        continue
    first, second = 0, 0
    nums = re.findall(r"(\d)", word)
    for i in range(len(nums)):
        if i % 2 == 0:
            first += int(nums[i])
        else:
            second += int(nums[i])
    if (first - second) % 3 == 0:
        print(word)






""" 


Признак делимости на 3 в двоичной системе счисления звучит следующим образом:

 «Число делится на 3 тогда и только тогда, когда сумма его цифр стоящих на четных местах отличается от суммы цифр,
 
  стоящих на нечетных местах, на число, делящееся на 3». Это признак 11-типа. Например, 2110 = 101012 """