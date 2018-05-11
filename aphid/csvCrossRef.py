#! /usr/bin/python3

import csv

compdict = {}
i = 0

with open('C:\\Users\Thompson\Documents\mpe.csv', 
          newline = '') as fone,  open('C:\\Users\Thompson\Documents\pred.csv', 
          newline = '') as ftwo:
    onecsv = csv.reader(fone, delimiter = ',')
    twocsv = csv.reader(ftwo, delimiter = ',')
    oneheader = next(onecsv)
    twoheader = next(twocsv)
    for onerow in onecsv:
        compdict[onerow[0]] = onerow
    for tworow in twocsv:
        if tworow[0] in compdict:
            print(tworow[0])
            i+=1
print(i)