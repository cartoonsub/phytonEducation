import csv
from datetime import datetime


collection = {}
with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\Crimes.csv', 'r') as file:
    rows = csv.reader(file)
    for row in rows:
        rawDate = row[2]
        try:
            date = (datetime.strptime(rawDate, "%m/%d/%Y %I:%M:%S %p"))
            year = (datetime.date(date).year)
            if year != 2015:
                continue
            primaryType = row[5]
            if primaryType in collection:
                collection[primaryType] += 1
            else:
                collection[primaryType] = 1
        except ValueError:
            print('Invalid date: ' + rawDate)
            continue

sorted_dict = {}
sorted_keys = sorted(collection, key=collection.get)
print(sorted_keys)
for w in sorted_keys:
    sorted_dict[w] = collection[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}