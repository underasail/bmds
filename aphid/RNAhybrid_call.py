#! /share/opt/python/3.6.5/bin/python

# USAGE = RNAhybrid_call.py [G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique.fa.annotations] [RNAhybrid.out]


from sys import argv
import csv
from subprocess import call

seq_dict = {}

with open(argv[1]) as f:
    csvreader = csv.reader(f, delimiter = ' ')
    for row in csvreader:
        if len(row) > 2:
            name = row[0].lstrip('>')
            seq = next(csvreader)[0]
            seq_dict.setdefault(name, []).append(seq)
with open(argv[2]) as f:
    csvreader = csv.reader(f, delimiter = ' ')
    for row in csvreader:
        if len(row) == 4:
            name = row[0]
            location = row[2]
            scale = row[3]
            seq_dict[name].append(location)
            seq_dict[name].append(scale)

for key, value in seq_dict.items():
    key = name
    seq = value[0]
    location = value[1]
    scale = value[2]
    call(['RNAhybrid', '-d', '%s,%s' % (location, scale), '-e', '0', '-p', '0.05', '-f', '2,8', '-m', '10000', \
          '-t', '/nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta', 
          seq, '>', 
          '/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/target_prediction/hybrid/\
          %s_targets.RNAhybrid' % (name)])
