#! /usr/bin/python

# runfile('C:/Users/Thompson/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/underasail/gitclones/bmds/aphid/isoformAnlaysis.py', wdir='C:/Users/Thompson/Documents')

import csv
from Bio import SeqIO

se_list = []
parent_list = []
scaffold_name_list = []
record_id_list = []
parent_id_list = []

with open('C:/Users/Thompson/Documents/miRNA_intersect.out.sort') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        scaffold = row[1].split(':')[0]
        start = row[1].split('-')[0].split(':')[1]
        end = row[1].split('-')[-1]
        mirna = row[0]
        se_list.append([scaffold, start, end, mirna])

#with open('C:/Users/Thompson/Documents/G006_Myzus_genome_ref_three_prime_utr_targets.fasta', 'w') as output_targets_fasta:
for entry in se_list:
    scaffold_1 = entry[0]
    start_1 = entry[1]
    end_1 = entry[2]
    mirna = entry[3]
    with open('C:/Users/Thompson/Documents/G006_Myzus_genome_ref_three_prime_utr.gff') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            scaffold_2 = row[0]
            start_2 = str(int(row[3]) - 1)
            end_2 = row[4]
            if scaffold_1 == scaffold_2 and start_1 == start_2 and end_1 == end_2:
                parent = row[8].split(';')[1]
                parent = parent.lstrip('Parent=')
                if parent not in parent_list:
                    parent_list.append(parent)
                    scaffold_name = '{0}:{1}-{2}'.format(scaffold_1, start_1, end_1)
                    scaffold_name_list.append(scaffold_name)
                    # print(mirna+'\t'+parent+'\t'+scaffold_1)
                else:
                    next(csvreader)
            else:
                pass
#parent_set = set(parent_list)
#scaffold_name_set = set(scaffold_name_list)
#for record in SeqIO.parse('C:/Users/Thompson/Documents/G006_Myzus_genome_ref_three_prime_utr.fasta', 'fasta'):
#    if record.id in scaffold_name_set:
#        parent_id = parent_list[scaffold_name_list.index(record.id)]
##            record.id = record.id + '\t{0}'.format(parent_id)
##            SeqIO.write(record, output_targets_fasta, 'fasta')
#        record_id_list.append(record.id)
#        parent_id_list.append(parent_id)
#    else:
#            pass

    
with open('C:/Users/Thompson/Documents/Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets.fa', 'w') as output_fasta:
    for record in SeqIO.parse('C:/Users/Thompson/Documents/Myzus_persicae_Clone_G006b_scaffolds.gff.pep.fa', 'fasta'):
        if record.id in parent_list:
            SeqIO.write(record, output_fasta, 'fasta')
        else:
            pass


    
