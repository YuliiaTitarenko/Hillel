# Використайте прикріплений файл csv та прочитайте його за допомогою модулю csv.
import csv
with open('SampleCSVFile_11kb.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))