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
                parent_list.append(parent)
                scaffold_name = '{0}:{1}-{2}'.format(scaffold_1, start_1, end_1)
                scaffold_name_list.append(scaffold_name)
                # print(mirna+'\t'+parent+'\t'+scaffold_1)
            else:
                pass
parent_set = set(parent_list)
scaffold_name_set = set(scaffold_name_list)
for record in SeqIO.parse('C:/Users/Thompson/Documents/G006_Myzus_genome_ref_three_prime_utr.fasta', 'fasta'):
    if record.id in scaffold_name_set:
        parent_id = parent_list[scaffold_name_list.index(record.id)]
#            record.id = record.id + '\t{0}'.format(parent_id)
#            SeqIO.write(record, output_targets_fasta, 'fasta')
        record_id_list.append(record.id)
        parent_id_list.append(parent_id)
    else:
        pass


cogs_dict_g = {}  # holds genome COGs; turns to percentages

cogs_dict = {}  # holds targets COGs; turns to percentages
cogs_per = []  # used for plotting target composition percentages in order

cogs_dict_final = {}  # holds target - genome percentages with labels
labels_final = []  # holds ordered labels
cogs_per_final = []   # used for plotting target - genome composition percentages in order

probs = []  # holds probability (weights) for each COG in genome
probs_dict = {}  # probability with label
pvals_raw = []
ci = []  # holds confidence intervals

#filelist = ["myseq0.fa.emapper.annotations", "myseq27000.fa.emapper.annotations", 
#            "myseq13500.fa.emapper.annotations", "myseq4500.fa.emapper.annotations", 
#            "myseq18000.fa.emapper.annotations", "myseq9000.fa.emapper.annotations", 
#            "myseq22500.fa.emapper.annotations"]
#            # target COG files
#total_g = 0
#for file in filelist:
#    with open(file) as f:
#        csvreader = csv.reader(f, delimiter = '\t')
#        header = next(csvreader)
#        for row in csvreader:
#            cog = row[11]
#            name = row[0]
##            name = name.split('.')[1]
#            if cog == "S":
#                next(csvreader)
#            else:
#                total_g = total_g + 1
#                # actual total number instead of total which includes proteins 
#                # multiple times for each COG assigned
#                if len(cog) > 1:
#                    cogs_list_g = cog.split(', ')  # because entries can match to multiple COGs
#                    for entry in cogs_list_g:
##                        cogs_dict_g.setdefault(entry, []).append(name)
#                        cogs_dict_g.setdefault(entry, []).append(record_id_list[parent_id_list.index(name)])
#                else:
##                    cogs_dict_g.setdefault(cog, []).append(name)
#                    cogs_dict_g.setdefault(cog, []).append(record_id_list[parent_id_list.index(name)])
#total_g = 0
#for key in cogs_dict_g:
#    cogs_dict_g[key] = set(cogs_dict_g[key])
#    total_g = total_g + len(set(cogs_dict_g[key]))
#total_t = 0
with open('Myzus_persicae_Clone_G006b_scaffolds.gff.pep_targets.fa.emapper.annotations') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    header = next(csvreader)
    for row in csvreader:
        cog = row[11]
        name = row[0]
#        name = name.split('.')[1]
        if cog == 'S':
            next(csvreader)
        else:
#            total_t = total_t + 1
            if len(cog) > 1:
                cogs_list = cog.split(', ')
                for entry in cogs_list:
#                    cogs_dict.setdefault(entry, []).append(name)
                    cogs_dict.setdefault(entry, []).append(record_id_list[parent_id_list.index(name)])
            else:
#                cogs_dict.setdefault(cog, []).append(name)
                cogs_dict.setdefault(cog, []).append(record_id_list[parent_id_list.index(name)])
total_t = 0
for key in cogs_dict:
#    cogs_dict[key] = set(cogs_dict[key])
#    total_t = total_t + len(set(cogs_dict[key]))
    total_t = total_t + len(cogs_dict[key])
# these create dictionaries with the COG letters as keys and proteins as values

labels = ["RNA processing and modification", "Chromatin structure and dynamics", 
          "Energy production and conversion", 
          "Cell cycle control, cell division,\nchromosome partitioning", 
          "Amino acid transport and metabolism", "Nucleotide transport and metabolism", 
          "Carbohydrate transport and metabolism", "Coenzyme transport and metabolism", 
          "Lipid transport and metabolism", 
          "Translation, ribosomal structure,\nand biogenesis", 
          "Transcription", "Replication, recombination, and repair", 
          "Cell wall/membrane/envelope biogenesis", "Cell motility", 
          "Posttranslational modification,\nprotein turnover, chaperones", 
          "Inorganic ion transport\nand metabolism", 
          "Secondary metabolites biosynthesis,\ntransport, and catabolism", 
          "Signal transduction mechanisms", 
          "Intracellular trafficking, secretion,\nand vesicular transport", 
          "Defense mechanisms", "Extracellular structures", 
          "Nuclear structure", "Cytoskeleton"]
          # COG long form labels over letters

labels_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "T", "U", "V", "W", "Y", "Z"]
                  # COG short form letters in the same order as labels

for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict[long_form] = cogs_dict.pop(short_form)  # exchanges letter COG for label
        cogs_dict[long_form] = len(cogs_dict[long_form])
        # creates percentage from number of values (proteins) over the total
    except KeyError:
        pass
not_in_targets = ["Defense mechanisms", "Coenzyme transport and metabolism", "Cell motility"]
                  # these entries show up in the genome proteins but not targets
                  # this sorts it out for the figure production
for entry in not_in_targets:
    cogs_dict[entry] = 0


for (long_form, short_form) in zip(labels, labels_letters):
    try:
        cogs_dict_g[long_form] = cogs_dict_g.pop(short_form)
        cogs_dict_g[long_form] = len(cogs_dict_g[long_form])
#        cogs_dict_final[long_form] = cogs_dict[long_form] - cogs_dict_g[long_form]
    except KeyError:
        pass