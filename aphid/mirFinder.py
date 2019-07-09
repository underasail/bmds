#! /usr/bin/python3

# 13314.48 seconds to run (3.7 hours)

import time
start_time = time.time()

import csv
import regex
import pickle
from joblib import Parallel, delayed 
import multiprocessing

m_s_dict = {}
nt_vars_set = set()
mirs = set()
reads_dict = {}
combined_reads_dict = {}
lowers = []

filenames = ['ShortStack-miRBase_37-46_56-58_12_19_m-s-per_len.csv']

for file in filenames:
    with open(file, 'r') as f:
        csvreader = csv.reader(f, delimiter = ',')
        for row in csvreader:
            lowers.append([row[3], row[0]])
            lowers.append([row[5], row[0]])
            
            cluster = row[0]
            per_map = row[1]
            m_len = row[2]
            mature = row[3].upper().replace('U', 'T')
            m_reads = row[4]
            star = row[5].upper().replace('U', 'T')
            s_reads = row[6]
            s_len = row[7]
            m_1nt = row[8].upper().replace('U', 'T')
            s_1nt = row[9].upper().replace('U', 'T')
            precursor = row[10]
            sec_struct = row[11]
            location = row[12]
            strand = row[13]
            sseqid = row[17]
            
            m_s_dict.setdefault(cluster, []).append(mature)
            m_s_dict.setdefault(cluster, []).append(star)
            m_s_dict.setdefault(cluster, []).append(m_1nt)
            m_s_dict.setdefault(cluster, []).append(s_1nt)
            m_s_dict.setdefault(cluster, []).append(precursor)
            m_s_dict.setdefault(cluster, []).append(sec_struct)
            m_s_dict.setdefault(cluster, []).append(sseqid)
            m_s_dict.setdefault(cluster, []).append(location)
            m_s_dict.setdefault(cluster, []).append(strand)
            nt_vars_set.add(m_1nt)
            nt_vars_set.add(s_1nt)
            mirs.add(mature)
            mirs.add(star)

start2_time = time.time()
print('Set-up done: {} seconds'.format(round(start2_time - start_time, 2)))

nt_vars_string = ''.join(nt_vars_set)

#mirFinderOutFiles = ['mirFinder_master_G006_Gut_plants_corrected.out', 
#                     'mirFinder_master_G002_Gut_plants_corrected.out', 
#                     'mirFinder_master_BTIRed_Gut_plants_corrected.out']

#reads_files = ['C:\\Users\\Thompson\\Documents\\reads\\G006_Gut_plants-only_corrected.fasta', 
#               'C:\\Users\\Thompson\\Documents\\reads\\G002_Gut_plants-only_corrected.fasta', 
#               'C:\\Users\\Thompson\\Documents\\reads\\BTIRed_Gut_plants-only_corrected.fasta']

reads_files = ['C:\\Users\\Thompson\\Documents\\reads\\G006_Bac_plants-only_corrected.fasta', 
               'C:\\Users\\Thompson\\Documents\\reads\\G002_Bac_plants-only_corrected.fasta', 
               'C:\\Users\\Thompson\\Documents\\reads\\BTIRed_Bac_plants-only_corrected.fasta']

#dict_strings = ['G006_reads_dict', 'G002_reads_dict', 'BTIRed_reads_dict']

#def mir_search(mir_out, reads_file, dict_string):
##    for mir_out, reads_file, dict_string in zip(mirFinderOutFiles, reads_files, dict_strings):
#    #    reads_dict = {}
#    #    with open(mir_out, 'w') as f_out,
#    with open(reads_file, 'r') as f:
#        csvreader = csv.reader(f, delimiter = '\t')
#        for row in csvreader:
#            header = row[0]
#            read_num = header.lstrip('>')
#            seq = next(csvreader)[0]
#            mirs = regex.findall('(%s){s<=1}' % (seq), nt_vars_string)
#            if len(mirs) > 0:
#                for cluster in m_s_dict.keys():
#                    mature = m_s_dict[cluster][0]
#                    star = m_s_dict[cluster][1]
#                    m_1nt = m_s_dict[cluster][2]
#                    s_1nt = m_s_dict[cluster][3]
#                    sseqid = m_s_dict[cluster][6]
#                    location = m_s_dict[cluster][7]
#                    strand = m_s_dict[cluster][8]
#                    m_match = regex.findall('(%s){s<=1}' % (seq), m_1nt)
#                    s_match = regex.findall('(%s){s<=1}' % (seq), s_1nt)
#                    if len(m_match) > 0:
##                        f_out.write('{0}\t{1}\t{2}\tm_{3}\t{4}\t{5}t{6}\t{7}\n'.format(
##                                    read_num, seq, cluster, mature, m_match[0], 
##                                    sseqid, location, strand))
#                        entry = []
#                        entry.append(read_num)
#                        entry.append(sseqid)
#                        entry.append(cluster)
#                        entry.append(seq)
#                        entry.append('m_{}'.format(mature))
#                        entry.append(m_match[0])
#                        entry.append(location)
#                        entry.append(strand)
#                        reads_dict.setdefault(mature, []).append(entry)
##                        reads_dict.setdefault(read_num, []).append(sseqid)
##                        reads_dict[read_num].append(cluster)
##                        reads_dict[read_num].append(seq)
##                        reads_dict[read_num].append('m_{}'.format(mature))
##                        reads_dict[read_num].append(m_match[0])
##                        reads_dict[read_num].append(location)
##                        reads_dict[read_num].append(strand)
#                    elif len(s_match) > 0:
##                        f_out.write('{0}\t{1}\t{2}\ts_{3}\t{4}\t{5}t{6}\t{7}\n'.format(
##                                    read_num, seq, cluster, star, s_match[0], 
##                                    sseqid, location, strand))
#                        entry = []
#                        entry.append(read_num)
#                        entry.append(sseqid)
#                        entry.append(cluster)
#                        entry.append(seq)
#                        entry.append('s_{}'.format(star))
#                        entry.append(s_match[0])
#                        entry.append(location)
#                        entry.append(strand)
#                        reads_dict.setdefault(star, []).append(entry)
##                        reads_dict.setdefault(read_num, []).append(sseqid)
##                        reads_dict[read_num].append(cluster)
##                        reads_dict[read_num].append(seq)
##                        reads_dict[read_num].append('s_{}'.format(star))
##                        reads_dict[read_num].append(s_match[0])
##                        reads_dict[read_num].append(location)
##                        reads_dict[read_num].append(strand)
#                    else:
#                        pass
#            else:
#                pass
##    with open('{}.pkl'.format(dict_string), 'wb') as dict_file:
##        pickle.dump(reads_dict, dict_file, protocol = pickle.HIGHEST_PROTOCOL)
#    
#    return reads_dict
#
#num_cores = multiprocessing.cpu_count()
#num_jobs = 3
#reads_dicts = Parallel(n_jobs=num_jobs)(delayed(mir_search)(mir_out, reads_file, dict_string) for mir_out, reads_file, dict_string in zip(mirFinderOutFiles, reads_files, dict_strings))
#
#for reads_dict in reads_dicts:
#    for label in reads_dict.keys():
#        combined_reads_dict.setdefault(label, []).extend(reads_dict[label])
#
#with open('reads_dict_m_s.pkl', 'wb') as dict_file:
#    pickle.dump(combined_reads_dict, dict_file, protocol = pickle.HIGHEST_PROTOCOL)

#mid_time = time.time()
#print('All Done: {} seconds'.format(round(mid_time - start2_time, 2)))




#with open('G006_reads_dict.pkl', 'rb') as dict_file:
#    G006_reads_dict = pickle.load(dict_file)
#with open('G002_reads_dict.pkl', 'rb') as dict_file:
#    G002_reads_dict = pickle.load(dict_file)
#with open('BTIRed_reads_dict.pkl', 'rb') as dict_file:
#    BTIRed_reads_dict = pickle.load(dict_file)

#reads_files = ['./reads/G006_Gut_F_trimmed_17-35_plants.fasta', 
#               './reads/G002_Gut_trimmed_17-35_plants.fasta', 
#               './reads/BTIRed_Gut_trimmed_17-35_plants.fasta']
G006_reads_dict = {}
G002_reads_dict = {}
BTIRed_reads_dict = {}
#dicts = [G006_reads_dict, G002_reads_dict, BTIRed_reads_dict]
#dict_strings = ['G006_reads_dict', 'G002_reads_dict', 'BTIRed_reads_dict']



with open(reads_files[0], 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        header = row[0]
        read_num = header.lstrip('>')
        seq = next(csvreader)[0]
        if seq in mirs:
            G006_reads_dict.setdefault(seq, []).append(read_num)
        else:
            pass

with open(reads_files[1], 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        header = row[0]
        read_num = header.lstrip('>')
        seq = next(csvreader)[0]
        if seq in mirs:
            G002_reads_dict.setdefault(seq, []).append(read_num)
        else:
            pass

with open(reads_files[2], 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        header = row[0]
        read_num = header.lstrip('>')
        seq = next(csvreader)[0]
        if seq in mirs:
            BTIRed_reads_dict.setdefault(seq, []).append(read_num)
        else:
            pass

reads_dict = {}
for reads_file in reads_files:
    with open(reads_file, 'r') as f:
        csvreader = csv.reader(f, delimiter = '\t')
        for row in csvreader:
            header = row[0]
            read_num = header.lstrip('>')
            seq = next(csvreader)[0]
            if seq in mirs:
                reads_dict.setdefault(seq, []).append(read_num)
            else:
                pass

#%%

total = 0
lines = []
for k in reads_dict.keys():
    try:
        G006_len = len(G006_reads_dict[k])
    except KeyError:
        G006_len = 0
    try:
        G002_len = len(G002_reads_dict[k])
    except KeyError:
        G002_len = 0
    try:
        BTIRed_len = len(BTIRed_reads_dict[k])
    except KeyError:
        BTIRed_len = 0
#    print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(k, len(reads_dict[k]), len(k), G006_len, G002_len, BTIRed_len))
    total += len(reads_dict[k])
    line = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(k, len(k), G006_len, G002_len, BTIRed_len, len(reads_dict[k]))
    lines.append(line)

print_lines = []
with open('exact_mirs_wo-old.fa', 'r') as f:
    file_lines = f.readlines()

    for line in lines:
        line_seq = line.split('\t')[0]
        len_pls = len(print_lines)
#        for name in file_lines:
        for i in range(0, len(file_lines), 2):
            name = file_lines[i]
            seq = file_lines[i + 1].rstrip('\n')
            name = name.lstrip('>').rstrip('\n')
#            seq = next(file_lines).rstrip('\n')
            if line_seq == seq:
                line = "{0}\t{1}".format(name, line)
                print_lines.append(line)
        if len(print_lines) == len_pls:
            name = 'Not in Gut'
            line = "{0}\t{1}".format(name, line)
            print_lines.append(line)
#    for name in f:
#        name = name.lstrip('>').rstrip('\n')
#        seq = next(f).rstrip('\n')
#        len_pls = len(print_lines)
#        for line in lines:
#            if line.split('\t')[0] == seq:
#                line = "{0}\t{1}".format(name, line)
#                print_lines.append(line)
#            if len(print_lines) == len_pls:
#                name = 'Not in Gut'
#                line = "{0}\t{1}".format(name, line)
#                print_lines.append(line)
#with open('mirFinder.out', 'w') as f:
#    for line in print_lines:
#        f.write(line + '\n')
#        print(line)
#    print('Total: {0} reads'.format(total))
#    f.write('Total: {0} reads\n'.format(total))

mid_time = time.time()
print('All Done: {} seconds'.format(round(mid_time - start2_time, 2)))

#%%

prev_mirs = {}
with open('phloem-mirnas.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter = ',')
#    p_header = next(csvreader)
    for row in csvreader:
        p_name = row[0]
        p_seq = row[1]
        p_mir = row[2]
        prev_mirs.setdefault(p_name, []).append([p_mir, p_seq])

species_s = sorted(prev_mirs.keys())
i = 0
for line in print_lines:
    seq = line.split('\t')[1]
    found_list = [''] * len(species_s)
    for species in species_s:
        species_list = list(zip(*prev_mirs[species]))
        if seq in species_list[1]:
            sp_ind = species_s.index(species)
            seq_ind = species_list[1].index(seq)
            found_list[sp_ind] = species_list[0][seq_ind]
        else:
            pass
        print_lines[i] = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(line, 
                         found_list[0], found_list[1], found_list[2],
                         found_list[3], found_list[4], found_list[5])
    i += 1

with open('mirFinder_Bac.out', 'w') as f:
    f.write("Homolog\tmiRNA Sequence\tLength\tExact Matches In: G006\tG002\tUS"
            "DA\tTotal\tPreviously Found In: {0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(species_s[0], 
            species_s[1], species_s[2], species_s[3], species_s[4], 
            species_s[5]))
    for line in print_lines:
        f.write(line + '\n')
        print(line)
    print('Total: {0} reads'.format(total))
    f.write('Total: {0} reads\n'.format(total))
