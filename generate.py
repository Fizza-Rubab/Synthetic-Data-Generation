# Region
# Branch
# Department
# User
# Importer
# Exporter
# HSCODE
# Status
# Revenue
# Date

from faker import Faker
fake = Faker()
import datetime
import random
cols = ['Region', 'Branch', 'Department', 'User', 'Importer', 'Exporter', 'Hscode', 'Status', 'Revenue', 'Date' ]
data = []
for r in range(1, 101):
    print("r", r)
    for b in range(1, 301):
        # print("b", b)
        for d in range(1, 101):
            region = "{:03d}".format(r)
            branch = "{:03d}".format(b)
            dept = "{:03d}".format(d)
            importer = fake.name()
            exporter = fake.name()
            date = fake.date_between_dates(date_start=datetime.date(2020, 1, 1), date_end=datetime.date(2022, 12, 31)).strftime("%m/%d/%Y")
            revenue = random.randint(100000, 999999)
            status = random.choice(['Satisfactory', 'Unsatisfactory', 'Under Review'])
            hscode = "{:02d}".format(random.randint(1, 99)) + '.' + "{:02d}".format(random.randint(1, 99)) + '.' + "{:02d}".format(random.randint(1, 99)) + '.' + "{:02d}".format(random.randint(1, 99))
            user = random.randint(1, 550)
            # print([f"R-{region}", f"B-{region}-{branch}", f"D-{region}-{branch}-{dept}", user, importer, exporter, hscode, status, revenue, date])
            data.append([f"R-{region}", f"B-{region}-{branch}", f"D-{region}-{branch}-{dept}", user, importer, exporter, hscode, status, revenue, date])
            # break


import csv

with open("dummydata.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)


            

