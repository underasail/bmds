#! /share/opt/python/3.3.1/bin/python

# Usage: ./parseSAM.py [INPUT SAM BUCHNERA FILE] [INPUT SAM OTHER FILE] (> Results passed to stdout, redirect with carrot to generate output file)

from sys import argv
import csv
import matplotlib.pyplot as plot


genedict = {}

"""Parsing of Bowtie2 SAM Output"""
with open(argv[1], newline='') as f:
    next(f)
    next(f)
    next(f)
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if len(row) >= 14:
            if 'XM:i:0' or 'XM:i:1' or 'XM:i:2' in str(row):
                # use to select only for allignments with two or fewer mismatches
                readnum = row[0]
                refgen = row[2]
                seq = row[9]
                # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
                # Set up ref genome as key and append read numbers as values
                genedict.setdefault(readnum, []).append(refgen)
        else:
            pass

print('genedict done')

with open(argv[2], newline='') as f:
    next(f)
    next(f)
    next(f)
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if len(row) >= 14:
            if 'XM:i:0' or 'XM:i:1' or 'XM:i:2' in str(row):
                readnum = row[0]
                refgen = row[2]
                seq = row[9]
                try:
                    e = genedict[readnum]
                    genedict[readnum].append(refgen)                    
                except KeyError:
                    pass
        else:
            pass

histlist = []
for i in sorted(genedict, key = lambda values: len(genedict[values]), reverse=True):
    if len(genedict[i]) >= 3:
        histlist.append(len(genedict[i]))

plot.hist(histlist, bins = 10, histtype = 'bar', align = 'mid', color = 'red')
plot.savefig('~/temp/genenamehist.jpg', bbox_inches = 'tight')


