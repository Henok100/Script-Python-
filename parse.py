import csv
import time

with open('names.csv', 'r') as names:
    csv_reader = csv.reader(names)

    for line in csv_reader:
        print(line)
        time.sleep(2)