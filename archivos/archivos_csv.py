import csv
import sys

# print(sys.path)

with open("/home/franb/Codin/python/dalto/archivos/datas.csv") as datas:
    reader = csv.reader(datas)
    for row in reader:
        
        print(row[0])
        print(row[1])