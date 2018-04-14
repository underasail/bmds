#! /share/opt/python/3.3.1/bin/python3

from sys import argv
import csv

aphid = []
buchnera = []
plant = []

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

with open(argv[3], newline='') as f:
    plant_csv = csv.reader(f, delimiter = '\t')
    for row in plant_csv:
        if isInt(row[0]) and ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            plant.append(row[0])
plant = set(plant)

allabp = aphid & buchnera & plant
bothab = aphid & buchnera - allabp
bothap = aphid & plant - allabp
bothbp = buchnera & plant - allabp
aphid = aphid - bothab - bothap - allabp
buchnera = buchnera - bothab - bothbp - allabp
plant = plant - bothap - bothbp - allabp
unknown = totalreads - len(aphid) - len(buchnera) - len(plant) - len(bothab) - len(bothap) - len(bothbp) - len(allabp)

print('Aphid Only: %s' % str(len(aphid)))
print('Buchnera Only: %s' % str(len(buchnera)))
print('Plant Only: %s' % str(len(plant)))
print('Both Aphid and Buchnera: %s' % str(len(bothab)))
print('Both Aphid and Plant: %s' % str(len(bothap)))
print('Both Buchnera and Plant: %s' % str(len(bothbp)))
print('Aphid, Buchnera, and Plant: %s' % str(len(allabp)))
print('Unknown: %s' % str(unknown))
