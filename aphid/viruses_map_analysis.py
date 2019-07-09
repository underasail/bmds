import csv
import pickle
import json

header_tags = ['@HD', '@SQ', '@PG']
filenames = ["BTIRed_Bac_viruses2.map", "G002_Bac_viruses2.map", 
"G006_Bac_viruses2.map", "BTIRed_Gut_viruses2.map", 
"G002_Gut_viruses2.map", "G006_Gut_viruses2.map"]
files_dict = {}
files_dict_2 = {}
files_genomes = {}
files_genomes_2 = {}
org_names_dict = {}


with open('viruses2_org_names.pkl', 'rb') as f:
    viruses2_org_names = pickle.load(f)

for entry in viruses2_org_names:
    name = entry[0]
    nuc_acc = entry[1]
    description = entry[2]
#    org_names_dict[nuc_acc] = "{0}: {1}".format(nuc_acc, name)
    org_names_dict[nuc_acc] = name

for filename in filenames:
    seqs_dict = {}
    genomes_dict = {}
    with open(filename, 'r') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            tag = row[0]
            if tag in header_tags:
                pass
            elif ('XM:i:0' or 'XM:i:1') in str(row):
                print(row[13], row[14])
                read_num = row[0]
                nuc_acc = row[2]
                seq = row[9]
#                name = org_names_dict[nuc_acc]
                if seq in seqs_dict.keys():
#                try:
#                    e = seqs_dict[seq]
                    if nuc_acc in seqs_dict[seq].keys():
                        seqs_dict[seq][nuc_acc].append(read_num)
                    else:
                        seqs_dict[seq].setdefault(nuc_acc, []).append(read_num)
                else:
#                except:
                    entry = {}
                    entry.setdefault(nuc_acc, []).append(read_num)
                    seqs_dict.setdefault(seq, None)
                    seqs_dict[seq] = entry
                genomes_dict.setdefault(nuc_acc, []).append(seq)
            else:
                pass
    dataset = filename.rstrip('_viruses2.map')
    files_dict[dataset] = seqs_dict
    files_genomes[dataset] = genomes_dict
#%%
for filename in filenames:
    seqs_dict_2 = {}
    genomes_dict_2 = {}
    with open(filename, 'r') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            tag = row[0]
            if tag in header_tags:
                pass
            elif 'XM:i:0' in str(row):
                read_num = row[0]
                nuc_acc = row[2]
#                print(nuc_acc)
                seq = row[9]
                if seq in seqs_dict.keys():
#                try:
#                    e = seqs_dict_2[seq]
                    if nuc_acc in seqs_dict_2[seq].keys():
                        seqs_dict_2[seq][nuc_acc].append(read_num)
                    else:
                        seqs_dict_2[seq].setdefault(nuc_acc, []).append(read_num)
                else:
#                except:
                    entry = {}
                    entry.setdefault(nuc_acc, []).append(read_num)
                    seqs_dict_2.setdefault(seq, None)
                    seqs_dict_2[seq] = entry
                genomes_dict_2.setdefault(nuc_acc, []).append(seq)
            else:
                pass
    dataset = filename.rstrip('_viruses2.map')
    files_dict_2[dataset] = seqs_dict_2
    files_genomes_2[dataset] = genomes_dict_2
#%%
for dataset in files_dict.keys():
    seqs_dict = files_dict[dataset]
    seqs_dict_2 = files_dict_2[dataset]
    genomes_dict = files_genomes[dataset]
    genomes_dict_2 = files_genomes_2[dataset]
    print('\n', dataset, '\n')
#    for seq in seqs_dict.keys():
#        if len(seqs_dict[seq]) > 1:
#            keys = list(seqs_dict[seq].keys())
#            names = []
#            for key in keys:
#                name = org_names_dict[key]
#                names.append(name)
##            print(len(keys))
##            print(seq, '\n',
##                  '\t', names[0], '\n\t', len(seqs_dict[seq][keys[0]]), 
##                  '\n\t', names[1], '\n\t', len(seqs_dict[seq][keys[1]]))
##                  json.dumps(seqs_dict[seq], indent = 1))
#            print("{0}\t{1}\t{2}\t{3}".format(seq, names[0], 
#                                              len(seqs_dict[seq][keys[0]]), 
#                                                  names[1], 
#                                                  len(seqs_dict[seq][keys[1]])
#                                              )
#                  )
    
#    seqs_in_genome_w1_mm = len(seqs_dict.keys())
#    seqs_in_genome_w0_mm = len(seqs_dict_2.keys())
#    seqs_in_genome_w1_mm = seqs_in_genome_w1_mm - seqs_in_genome_w0_mm
#    print("{0}\t{1}\t{2}".format(dataset, seqs_in_genome_w1_mm, 
#                                 seqs_in_genome_w0_mm))
    
    for key in genomes_dict:
        genomes_dict[key] = list(set(genomes_dict[key]))
    for key_2 in genomes_dict_2:
        genomes_dict_2[key_2] = list(set(genomes_dict_2[key_2]))
    for nuc_acc in genomes_dict:
        name = org_names_dict[nuc_acc]
        unique_seqs_in_genome_w1_mm = len(genomes_dict[nuc_acc])
        try:
            unique_seqs_in_genome_w0_mm = len(genomes_dict_2[nuc_acc])
        except:
            print('{0} not in genomes_dict_2'.format(name))
        print("{0}\t{1}\t{2}".format(name, unique_seqs_in_genome_w1_mm, 
                                     unique_seqs_in_genome_w0_mm))
#    print(genomes_dict.keys())