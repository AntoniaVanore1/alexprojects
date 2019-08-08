import sys
import csv
import json
from faker import Faker

record_count = 1000
fake = Faker()
fieldnames = ['ID', 'firstName', 'lastName', 'zipCode'] 

def create_csv_file():
    with open('database.csv', 'w', newline='') as f:

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(record_count):
            writer.writerow(
                {
                    'ID': fake.random_int(min=100, max=5000),
                    'firstName': fake.first_name(),
                    'lastName': fake.last_name(),
                    'zipCode': fake.zipcode()
                }
            )

create_csv_file()
csvfile = open('database.csv', 'r')

with open('database.csv') as f:
    for row in csv.DictReader(csvfile, fieldnames):
        with open(row['ID'] + '.json', 'w') as jsonfile:
            print(json.dumps(row))
            json.dump(row, jsonfile)
       


