#! /share/opt/python/3.3.1/bin/python

# USAGE = ./perGenomes.py [SAM FILE] [/root/path/to/percentage_output.tsv]

from sys import argv
import csv

primary = ['Buchnera', 'Myzus']
secondary = ['plants', 'other_bacteria', 'viruses']
genomes_dict = {}

if 'G002' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 3427212
        elif any(word in argv[1] for word in primary):
            totalreads = 12085742
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 5942393
        elif any(word in argv[1] for word in primary):
            totalreads = 9032198
elif 'G006' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 2054109
        elif any(word in argv[1] for word in primary):
            totalreads = 21960873
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 1530897
        elif any(word in argv[1] for word in primary):
            totalreads = 2626650
elif 'BTIRed' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 3999644
        elif any(word in argv[1] for word in primary):
            totalreads = 13931847
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 6570398
        elif any(word in argv[1] for word in primary):
            totalreads = 9064708

with open(argv[1], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if len(row) >= 14 and 'XM:i:0' in str(row):
            # used to select only for allignments with no mismatches
            # length factor skips header rows also
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
            genomes_dict.setdefault(refgen, []).append(readnum)
            # allows entry to be created if not and added to without disruption
            # if previously generated
        else:
            pass
with open(argv[2], 'w') as f:
    f.write('%s\t\t' % (argv[1]))
    f.write('Percentage\tNumber of reads\tFilename')
    for refgen, readnums in genomes_dict.items():
        count = len(readnums)
        genomes_dict[refgen].append(count)
        # Appends a new entry to end of readnums list with 
        # the number of matched reads for that genome
        percent = round(((int(readnums[-1])/totalreads)*100), 4)
        # Calculates the percent of total reads mapped to that ggenome
        genomes_dict[refgen].append(percent)
        # genomes_dict[genome] = {read1, read2, ... , count, percentage}
        f.write('%s%%\t%s\t%s' % (percent, count, argv[2]))
