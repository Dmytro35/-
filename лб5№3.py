import csv
import sys
print("1 група")
filename = "1 група.txt"
fd = open(filename,"r")
reader = csv.reader(fd,delimiter = "\t")
for row in reader:
    print(row)

print("2 група")
filename = "2 група.txt"
fd = open(filename,"r")
reader = csv.reader(fd,delimiter = "\t")
for row in reader:
    print(row)

import csv
with open("1 група.txt") as file:
    csv_reader = csv.reader(file)
    sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)

for name, score in sorted_list:
    print("{0}'s Score = {1}".format(name, score))
    fd.close()

with open("2 група.txt") as file:
    csv_reader = csv.reader(file)
    sorted_list = sorted(csv_reader, key=lambda row: int(row[1]), reverse=True)

for name, score in sorted_list:
    print("{0}'s Score = {1}".format(name, score))
    fd.close()

input()

