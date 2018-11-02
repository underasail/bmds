#! /share/opt/python/3.6.5/bin/python

# USAGE: ./percentage_calculations.py [APHID/BUCHNERA SAM FILE] > [DESIRED OUTPUT FILE]

from sys import argv
import csv

matched_dict = {}
aphid = set()
buchnera = set()
plant = set()

with open(argv[1], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            # with scaffold header lines, would need too many next()
            # this will skip header lines too
            # also selects for alignments with one mismatch or fewer
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
            if '__len__' in refgen:
                refgen = 'buchnera'
                buchnera.add(readnum)
            elif 'scaffold_' in refgen:
                refgen = 'aphid'
                aphid.add(readnum)
            else:
                refgen = 'plant'
                plant.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
            # allows key to be created if not already and added to without disruption
            # if previously generated
        else:
            pass

with open(argv[2], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            # with scaffold header lines, would need too many next()
            # this will skip header lines too
            # also selects for alignments with one mismatch or fewer
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
            if '__len__' in refgen:
                refgen = 'buchnera'
                buchnera.add(readnum)
            elif 'scaffold_' in refgen:
                refgen = 'aphid'
                aphid.add(readnum)
            else:
                refgen = 'plant'
                plant.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
            # allows key to be created if not already and added to without disruption
            # if previously generated
        else:
            pass

with open(argv[3], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            # with scaffold header lines, would need too many next()
            # this will skip header lines too
            # also selects for alignments with one mismatch or fewer
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
            if '__len__' in refgen:
                refgen = 'buchnera'
                buchnera.add(readnum)
            elif 'scaffold_' in refgen:
                refgen = 'aphid'
                aphid.add(readnum)
            else:
                refgen = 'plant'
                plant.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
            # allows key to be created if not already and added to without disruption
            # if previously generated
        else:
            pass

print('Total: ', len(aphid | buchnera | plant))
print('All: ', len(aphid & buchnera & plant))
print('Aphid and plant: ', len((aphid & plant) - buchnera))
print('Aphid and Buchnera: ', len((aphid & buchnera) - plant))
print('Buchnera and Plant: ', len((buchnera & plant) - aphid))
print('Aphid: ', len(aphid - buchnera - plant))
print('Buchnera: ', len(buchnera - aphid - plant))
print('Plant: ', len(plant - aphid - buchnera))

