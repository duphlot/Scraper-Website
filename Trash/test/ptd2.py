import csv
with open('lgh.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)