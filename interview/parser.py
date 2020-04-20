import csv

with open("address.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        if row[3] == "Ontario":
            print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}.')
            line_count += 1
            