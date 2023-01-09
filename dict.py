import csv
import time

csv_filename = 'names.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(str(row))
        time.sleep(2)
