#! /usr/bin/python3

import csv
import regex

nt_vars = {}
nt_vars_set = set()
results = []

#with open('SS_SRR37-46_m-s-per_len.txt', 'r') as f:
with open('ShortStack_SRR56-58_m-s-per_len.txt', 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        cluster = row[0]
        per_map = row[1]
        m_len = row[2]
        mature = row[3].replace('U', 'T')
        m_reads = row[4]
        star = row[5].replace('U', 'T')
        s_reads = row[6]
        s_len = row[7]
        m_1nt = row[8].replace('U', 'T')
        s_1nt = row[9].replace('U', 'T')
        
        nt_vars.setdefault(cluster, set()).add(m_1nt)
        nt_vars.setdefault(cluster, set()).add(s_1nt)

for mirs in nt_vars.values():
    nt_vars_set = nt_vars_set.union(mirs)

nt_vars_string = ''.join(nt_vars_set)

with open('C:\\Users\\Thompson\\Documents\\reads\\G006_Gut_F_trimmed_17-35_plants.fasta', 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        header = row[0]
        seq = next(csvreader)[0]
        mirs = regex.findall('(%s){s<=1}' % (seq), nt_vars_string)
        if len(mirs) > 0:
            for cluster in nt_vars.keys():
                mir_match = regex.findall('(%s){s<=1}' % (seq), ''.join(nt_vars[cluster]))
                if len(mir_match) > 0:
                    print('{0}\t{1}\t{2}\t{3}'.format(header.lstrip('>'), seq, cluster, mir_match[0]))
                    results.append(seq)
                else:
                    pass
