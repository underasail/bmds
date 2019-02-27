#! /usr/bin/python3

from sys import argv
import csv
import re

#argv = ['ShortStackMDirtoSS.py', 'C:\\Users\\Thompson\\Documents\\ShortStack_6_20-24_f_300_SRA_q28_17-25_SRR799356-58.ss']

with open(argv[1]) as f:
    csvreader = csv.reader(f, delimiter = ' ')
    for row in csvreader:
        header = row
        seq = next(csvreader)[0]
        seq_len = len(seq)
        struct = next(csvreader)[0]
        mature_full = next(csvreader)[0]
        mature = mature_full.strip('.')
        mature_M = re.sub('[AGCU]', 'M', mature_full)
        star_full = next(csvreader)[0]
        star = star_full.strip('.')
        star_S = re.sub('[AGCU]', 'S', star_full)
        next(csvreader)
        
        m_start = mature_full.index(mature)
        m_end = mature_full.index(mature) + len(mature)
        s_start = star_full.index(star)
        s_end = star_full.index(star) + len(star)
        
        if mature_M.index('M') < star_S.index('S'):
            mature_M = mature_M.rstrip('.')
            star_S = star_S[m_end:]
            mirstrand = mature_M + star_S
        
        elif mature_M.index('M') > star_S.index('S'):
            star_S = star_S.rstrip('.')
            mature_M = mature_M[s_end:]
            mirstrand = star_S + mature_M
        else:
            pass
        
        print(' '.join(header))
        print(seq)
        print(struct)
        print(mirstrand)
        