#! /usr/bin/python3

from sys import argv
import csv
import regex

rows = []
mature_winone = []
star_winone = []
m_s_readcount = 0
#argv = ['75_miR-PREFeR.py', 'Cluster_22854_Y.txt']
total = 0

with open(argv[1], 'r') as f:
    csvreader = csv.reader(f, delimiter = ' ')
    row = next(csvreader)
    mirna = row[0]
    next(csvreader)
    seq_row = next(csvreader)
    precursor = seq_row[0]
#    precursor = seq_row[0].replace('U', 'T')
    sec_struct = next(csvreader)[0]

    mature_row = next(csvreader)
    mature = mature_row[0].strip('.')
    m_reads = int(mature_row[3].lstrip('a='))
    total += m_reads
    m_s_readcount += m_reads
    try:
        m_start = precursor.index(mature)
        m_end = m_start + len(mature)
    except ValueError:
        mature_adj = regex.findall('(%s){s<=1}' % (mature), precursor)[0]
        m_start = precursor.index(mature_adj)
        m_end = m_start + len(mature)
        
    star_row = next(csvreader)
    star = star_row[0].strip('.')
    s_reads = int(star_row[3].lstrip('a='))
    total += s_reads
    m_s_readcount += s_reads
    try:
        s_start = precursor.index(star)
        s_end = s_start + len(star)
    except ValueError:
        star_adj = regex.findall('(%s){s<=1}' % (star), precursor)[0]
        s_start = precursor.index(star_adj)
        s_end = s_start + len(star)
    except:
        print(argv[1])
    
    next(csvreader)
    for row in csvreader:
        if len(row) == 3:
            reads = int(row[2].lstrip('a='))
            total += reads
            if row[0][0] == '.' or row[0][-1] == '.':
                seq = row[0].strip('.')
            elif row[0][0] == '<' or row[0][-1] == '<':
                seq = row[0].strip('<')
            else:
                pass
            try:
                seq_start = precursor.index(seq)
                seq_end = seq_start + len(seq)
                if (m_start - 1 <= seq_start <= m_start + 1) and (m_end - 1 <= seq_end <= m_end + 1):
                    reads = int(row[2].lstrip('a='))
                    mature_winone.append([seq, reads])
                    m_s_readcount += reads
                elif (s_start - 1 <= seq_start <= s_start + 1) and (s_end - 1 <= seq_end <= s_end + 1):
                    reads = int(row[2].lstrip('a='))
                    star_winone.append([seq, reads])
                    m_s_readcount += reads
            except ValueError:
                pass
            except:
                print('Unaccounted for error in: {}'.format(argv[1]))
        else:
            pass

m_s_per_mapped = round(m_s_readcount*100/total, 2)
#print('Precursor: {0}\nPercent reads mapped to mature & star: {1}%\n'.format(argv[1].rstrip('.map.txt'), m_s_per_mapped))
print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(argv[1].rstrip('_Y.txt'), m_s_per_mapped, 
                                               len(mature), mature, m_reads, star, s_reads, 
                                               len(star)))
# print format: precursor name  percent of 1nt variants mapped to miRNA/miRNA*  length of mature miRNA

