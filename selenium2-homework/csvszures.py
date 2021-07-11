import csv

csvwrite = open("table_szures.csv", "w", encoding="utf-8")
with open("table_in.csv", encoding="utf-8") as csvf:
    csvreader = csv.reader(csvf)
    print("Email,Name", file=csvwrite)
    next(csvreader)
    for row in csvreader:
        print(row[1].strip(' ') + "," + row[0].strip(' '), file=csvwrite)
csvwrite.close()
