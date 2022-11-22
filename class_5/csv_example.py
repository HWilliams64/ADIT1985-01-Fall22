import csv

with open('./heros.csv', 'r', newline='') as file:
    reader = csv.reader(file, dialect='excel')

    for row in reader:
        print(' '.join(row[1:3]))