#! /usr/bin/python

import csv
from Bio import SeqIO

se_list = []
parent_list = []

with open('miRNA_intersect.out.sort') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        scaffold = row[1].split(':')[0]
        end = row[1].split('-')[-1]
        mirna = row[0]
        se_list.append([scaffold, end, mirna])

for entry in se_list:
    scaffold_1 = entry[0]
    end_1 = entry[1]
    mirna = entry[2]
    with open('G006_Myzus_genome_ref_three_prime_utr.gff') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            scaffold_2 = row[0]
            end_2 = row[4]
            if scaffold_1 == scaffold_2 and end_1 == end_2:
                parent = row[8].split(';')[1]
                parent = parent.lstrip('Parent=')
                parent_list.append(parent)
                # print(mirna+'\t'+parent+'\t'+scaffold_1)
            else:
                pass
parent_set = set(parent_list)
with open('Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets.fa', 'w') as output_fasta:
    for record in SeqIO.parse('Myzus_persicae_Clone_G006b_scaffolds.gff.pep.fa', 'fasta'):
        if record.id in parent_set:
            SeqIO.write(record, output_fasta, 'fasta')
        else:
            pass


    
