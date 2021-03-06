#! /share/opt/python/3.3.1/bin/python3

from sys import argv
import csv

aphid = []
buchnera = []

if 'Bac' in argv[1]:
    totalreads = 21960873
elif 'Gut' in argv[1]:
    totalreads = 2626650
else:
    pass

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

with open(argv[1], newline='') as f:
    aphid_csv = csv.reader(f, delimiter = '\t')
    for row in aphid_csv:
        if isInt(row[0]) and ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            aphid.append(row[0])
aphid = set(aphid)

with open(argv[2], newline='') as f:
    buchnera_csv = csv.reader(f, delimiter = '\t')
    for row in buchnera_csv:
        if isInt(row[0]) and ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            buchnera.append(row[0])
buchnera = set(buchnera)

both = aphid & buchnera
aphid = aphid - both
buchnera = buchnera - both
unknown = totalreads - len(aphid) - len(buchnera) - len(both)

print('Aphid Only: %s' % str(len(aphid)))
print('Buchnera Only: %s' % str(len(buchnera)))
print('Both: %s' % str(len(both)))
print('Unknown: %s' % str(unknown))
