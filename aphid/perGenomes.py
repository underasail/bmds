#! /share/opt/python/3.6.5/bin/python

# USAGE = ./perGenomes.py [SAM FILE] [/root/path/to/percentage_output.tsv]

from sys import argv
import csv
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'mct30@miami.edu'

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
        if (len(row) >= 14) and ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            # used to select only for allignments with zero or one mismatches
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

genbank_accession_numbers = list(genomes_dict.keys())
efetch_handle = Entrez.efetch(db = 'nuccore', id = genbank_accession_numbers, rettype = 'gb', retmode = 'text')
efetch_records = SeqIO.parse(efetch_handle, 'gb')
# Search all accession numbers at once to avoid API search limits at NCBI
for (record, genbank_accession_number) in zip(efetch_records, genbank_accession_numbers):
    organism_name = record.annotations['organism']
    record_GBA = str(record.annotations['accessions'][0])
    if record_GBA in str(genbank_accession_number):
        genomes_dict[organism_name] = genomes_dict.pop(genbank_accession_number)
    else:
        print('Records not aligned')
    # Pulls the organism name from the annotations of the SeqRecord 
    # object to identify the genome later on in output files
    ##genomes_dict[organism_name].append(record.description)
    # Added description to end of readnums list because it contains strain and genome info
    print(organism_name)

with open(argv[2], 'w') as f:
    f.write('%s\t\t\t\n' % (argv[1]))
    f.write('Percentage\tNumber of Reads\tOrganism Name\tDescription\n')
    for refgen, readnums in genomes_dict.items():
        count = len(readnums) - 1
        # -1 accounts for added description at the end
        genomes_dict[refgen].append(count)
        # Appends a new entry to end of readnums list with 
        # the number of matched reads for that genome
        percent = round(((int(readnums[-1])/totalreads)*100), 4)
        # Calculates the percent of total reads mapped to that ggenome
        genomes_dict[refgen].append(percent)
        # genomes_dict[genome] = {read1, read2, ... , count, percentage}
        f.write('%s%%\t%s\t%s\t%s\n' % (percent, count, refgen, readnums[-3]))
