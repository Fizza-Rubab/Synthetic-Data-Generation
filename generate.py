from faker import Faker
fake = Faker()
import datetime
import random
cols = ['Region', 'Branch', 'Department', 'User', 'Importer', 'Exporter', 'Hscode', 'Status', 'Revenue', 'Date' ]
data = ['Region', 'Branch', 'Department', 'User', 'Importer', 'Exporter', 'Hscode', 'Status', 'Revenue', 'Date']
for r in range(1, 10):
    print("r", r)
    for b in range(1, 101):
        for d in range(1, 101):
            region = "{:03d}".format(r)
            branch = "{:03d}".format(b)
            dept = "{:03d}".format(d)
            importer = fake.name()
            exporter = fake.name()
            date = fake.date_between_dates(date_start=datetime.date(2020, 1, 1), date_end=datetime.date(2022, 12, 31)).strftime("%d/%m/%Y")
            revenue = random.randint(100000, 999999)
            status = random.choice(['Satisfactory', 'Unsatisfactory', 'Under Review'])
            hscode = "{:02d}".format(random.randint(1, 99))  + "{:02d}".format(random.randint(1, 99)) + '-' + "{:02d}".format(random.randint(1, 99)) + "{:02d}".format(random.randint(1, 99))
            user = random.randint(1, 550)
            data.append([f"R-{region}", f"B-{region}-{branch}", f"D-{region}-{branch}-{dept}", user, importer, exporter, hscode, status, revenue, date])
            

import csv

with open("dummydata3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


            

