import csv

        
books = [
    ['python', 'java', 'c++', 'c#', 'ruby', 12.42],
    ['Pushkin', 'Tolstoy', 'Dostoevsky', 'Lenin', 'Stalin'],
 ]
with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\csvWrite.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(books)
    for book in books:
        print(book)
        writer.writerow(book)


print('\n')
with open('C:\\phytonProjects\\phytonEducation\\firstStep\\part3Request\\static\\csvWrite.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)