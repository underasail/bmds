#! /usr/bin/python3

import csv

compdict = {}
final = []

with open('C:\\Users\Thompson\Documents\mpe.csv') as fone, \
     open('C:\\Users\Thompson\Documents\pred.csv') as ftwo:
    onecsv = csv.reader(fone, delimiter = ',')
    twocsv = csv.reader(ftwo, delimiter = ',')
    # oneheader = next(onecsv)
    # twoheader = next(twocsv)
    for onerow in onecsv:
        compdict[onerow[0]] = onerow
    for tworow in twocsv:
        if tworow[0] in compdict:
            print(tworow[0])
            final.append(tworow[0])
final = set(final)
print(len(final))