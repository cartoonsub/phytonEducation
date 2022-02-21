count = int(input())
if (count % 10 == 0):
    phrase = str(count) + ' программистов'
    print(phrase)
elif ((count % 10 == 1) and (count % 100 != 11)):
    phrase = str(count) + ' программист'
    print(phrase)
elif ((count % 100 == 12) or (count % 100 == 13) or (count % 100 == 14)):
    phrase = str(count) + ' программистов'
    print(phrase)
elif ((count % 10 == 2) or (count % 10 == 3) or (count % 10 == 4)):
    phrase = str(count) + ' программиста'
    print(phrase)
else:
    phrase = str(count) + ' программистов'
    print(phrase)