#! /usr/bin/python3
#%%
from sys import argv
import csv

# USAGE: 
#     cd ./miR-PREFeR_predictions/readmapping
#     for file in miRNA-precursor_*; do 
#         ../75_miR-PREFeR.py $file; 
#         done > m-s-per_len.tsv

rows = []
mature_winone = []
star_winone = []
m_s_readcount = 0
#argv = ['75_miR-PREFeR.py', 'miRNA-precursor_154.map.txt']

with open(argv[1], 'r') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    row = next(csvreader)
    mirna = row[0].split(' ')[0].lstrip('>')
    next(csvreader)
    next(csvreader)
    seq_row = next(csvreader)
    total = int(seq_row[1].lstrip('total_mapped_reads='))
    precursor = seq_row[0].replace('U', 'T')
    sec_struct = next(csvreader)
    for row in csvreader:
        rows.append(row)
        if row[0][0] == 'm' or row[0][-1] == 'm':
            reads = int(row[1].split(', ')[0].lstrip('depth='))
            mature = row[0].strip('m')
#            mature_winone.append([mature, reads])
#            m_s_readcount += reads
            m_start = precursor.index(mature)
            m_end = m_start + len(mature)
#            mature is precursor[m_start:m_end]
        elif row[0][0] == 's' or row[0][-1] == 's':
            reads = int(row[1].split(', ')[0].lstrip('depth='))
            star = row[0].strip('s')
#            star_winone.append([star, reads])
#            m_s_readcount += reads
            s_start = precursor.index(star)
            s_end = s_start + len(star)
        else:
            pass

for row in rows:
    character = row[0][0]
    seq = row[0].strip(character)
    try:
        seq_start = precursor.index(seq)
        seq_end = seq_start + len(seq)
        if (m_start - 1 <= seq_start <= m_start + 1) and (m_end - 1 <= seq_end <= m_end + 1):
            reads = int(row[1].split(', ')[0].lstrip('depth='))
            mature_winone.append([seq, reads])
            m_s_readcount += reads
        elif (s_start - 1 <= seq_start <= s_start + 1) and (s_end - 1 <= seq_end <= s_end + 1):
            reads = int(row[1].split(', ')[0].lstrip('depth='))
            star_winone.append([seq, reads])
            m_s_readcount += reads
    except ValueError:
        pass
    except NameError:
        print('Unaccounted for error in: {}'.format(argv[1]))

m_s_per_mapped = round(m_s_readcount*100/total, 2)
#print('Precursor: {0}\nPercent reads mapped to mature & star: {1}%\n'.format(argv[1].rstrip('.map.txt'), m_s_per_mapped))
print('{0}\t{1}\t{2}'.format(argv[1].rstrip('.map.txt'), m_s_per_mapped, len(mature)))
# print format: precursor name  percent of 1nt variants mapped to miRNA/miRNA*  length of mature miRNA
#%%
