import csv, os

new_file = not os.path.isfile('personnel.csv')
mode = 'w' if new_file else 'a'

with open('personnel.csv', mode, newline='') as file:
    writer = csv.writer(file, dialect='excel')

    if new_file:
        writer.writerow(['FIRST NAME', 'LAST NAME'])

    while True:
        full_name = input("Please type your full name: ")

        if not full_name:
            break

        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        writer.writerow([first_name, last_name])
