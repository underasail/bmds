#! /share/opt/python/3.3.1/bin/python

from sys import argv
import csv

matched_reads_dict = {}

if 'G002' in argv[1]:
    if 'Bac' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 3427212
        elif ('Buchnera' or 'Myzus') in argv[1]:
            totalreads = 12085742
    elif 'Gut' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 5942393
        elif ('Buchnera' or 'Myzus') in argv[1]:
            totalreads = 9032198
elif 'G006' in argv[1]:
    if 'Bac' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 2054109
        elif ('Buchnera' or 'Myzus') in argv[1]:
            totalreads = 21960873
    elif 'Gut' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 1530897
        elif ('Buchnera' or 'Myzus') in argv[1]:
            totalreads = 2626650
elif 'BTIRed' and 'Bac' in argv[1]:
    if 'Bac' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 3999644
        elif ('Buchnera' or 'Myzus') in argv[1]:
            totalreads = 13931847
    elif 'Gut' in argv[1]:
        if ('plants' or 'other_bacteria' or 'viruses') in argv[1]:
            totalreads = 6570398
        elif ('Buchnera' or 'Myzus') in argv[1]:
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
            matched_reads_dict.setdefault(readnum, []).append(refgen)
            # allows entry to be created if not and added to without disruption
            # if previously generated
        else:
            pass

matched_reads_per = round((len(matched_reads_dict.keys())*100)/totalreads, 4)
# percent or reads that mapped perfectly to the genome

print('%s%%\t%s\t%s' % (matched_reads_per, totalreads, argv[1]))
            
            
            
