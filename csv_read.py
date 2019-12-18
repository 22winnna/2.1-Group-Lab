import csv
with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0] + " (" + str(row[1]) + ")")