import matplotlib
matplotlib.use('Agg')
import numpy as np
import csv
import pysam
import pysamstats
import matplotlib.pyplot as plt

names = []
seqs = []

mybam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G006_G002_BTIRed_Gut_plant-precursors_bowtie1_a_T.merged.sorted.bam')
G006_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G006_Gut_plant-precursors_bowtie1_a_T.sorted.bam')
G002_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G002_Gut_plant-precursors_bowtie1_a_T.sorted.bam')
BTIRed_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/BTIRed_Gut_plant-precursors_bowtie1_a_T.sorted.bam')

def pull_down(name, row):
    row[0] = '{0}_{1}'.format(name, row[0])
    csvwriter.writerow(row)
    rows.append(row)
    chrom = row[0]
    start = 1
#    chrom = row[12].split(':')[0]
#    start = int(row[12].split(':')[1].split('-')[0])
#    end = int(row[12].split(':')[1].split('-')[1])
    #row = ['csi-miR395c-3p_Cluster_151156', '86.36', '21', 'CUGAAGUGUUUGGGGGAACUC', '7', 'GUUCCUCUGAGCACUUCAUUG', '6', '21', 'ACUGAAGUGUUUGGGGGAACUCC', 'AGUUCCUCUGAGCACUUCAUUGG', 'UUGGUCGGAUGUCUCCUAGAGUUCCUCUGAGCACUUCAUUGGGUAUACAAUUUCUUAUGAAGAUUACCCACUGAAGUGUUUGGGGGAACUCCUGGACCCAUUCUACGGUUU']
#    mybam_lc = pysamstats.load_coverage(mybam, chrom = chrom, start = start, 
#                                        end = end)
    mybam_lc = pysamstats.load_coverage(mybam, chrom = chrom)
    G006_bam_lc = pysamstats.load_coverage(G006_bam, chrom = chrom)
    G002_bam_lc = pysamstats.load_coverage(G002_bam, chrom = chrom)
    BTIRed_bam_lc = pysamstats.load_coverage(BTIRed_bam, chrom = chrom)
    
    mature = row[3]
    star = row[5]
    precursor = row[10]
    end = len(precursor)
    if any(m.islower() for m in mature) or any(s.islower() for s in star):
        pass
    else:
        m_start = precursor.index(mature)
        m_end = m_start + len(mature)
        s_start = precursor.index(star)
        s_end = s_start + len(star)
    
#        if len(mybam_lc.pos) > 0:
        if (len(G006_bam_lc.pos) > 0) or (len(G002_bam_lc.pos) > 0) or \
        (len(BTIRed_bam_lc.pos) > 0):
            positions = np.arange(start, end + 1)
            read_counts = []
            
            G006_bam_lc_pos = list(G006_bam_lc.pos)
            for entry in positions:
                if entry in G006_bam_lc_pos:
                    read_counts.append(G006_bam_lc.reads_all[G006_bam_lc_pos.index(entry)])
                else:
                    read_counts.append(0)
                    
            G002_bam_lc_pos = list(G002_bam_lc.pos)
            for entry in positions:
                if entry in G002_bam_lc_pos:
                    pos_ind = entry - 1
                    read_counts[pos_ind] += G002_bam_lc.reads_all[G002_bam_lc_pos.index(entry)]
                else:
                    pass
            
            BTIRed_bam_lc_pos = list(BTIRed_bam_lc.pos)
            for entry in positions:
                if entry in BTIRed_bam_lc_pos:
                    pos_ind = entry - 1
                    read_counts[pos_ind] += BTIRed_bam_lc.reads_all[BTIRed_bam_lc_pos.index(entry)]
                else:
                    pass
            
            ax = plt.subplot(1, 1, 1)
            if m_start > s_start:
                plt.plot(positions[:s_start], read_counts[:s_start], 
                         color = 'black', label = 'Tails')
                plt.plot(positions[s_start:s_end+1], read_counts[s_start:s_end+1], 
                         color = 'red', label = 'Star')
                plt.plot(positions[s_end+1:m_start], read_counts[s_end+1:m_start], 
                         color = 'gold', label = 'Loop')
                plt.plot(positions[m_start:m_end+1], read_counts[m_start:m_end+1], 
                         color = 'green', label = 'Mature')
                plt.plot(positions[m_end+1:], read_counts[m_end+1:], 
                         color = 'black')
            elif s_start > m_start:
                plt.plot(positions[:m_start], read_counts[:m_start], 
                         color = 'black', label = 'Tails')
                plt.plot(positions[m_start:m_end+1], read_counts[m_start:m_end+1], 
                         color = 'green', label = 'Mature')
                plt.plot(positions[m_end+1:s_start], read_counts[m_end+1:s_start], 
                         color = 'gold', label = 'Loop')
                plt.plot(positions[s_start:s_end+1], read_counts[s_start:s_end+1], 
                         color = 'red', label = 'Star')
                plt.plot(positions[s_end+1:], read_counts[s_end+1:], 
                         color = 'black')
            plt.legend()
            ind = np.arange(max(read_counts) + 1)
            plt.yticks(ind, ind)
            plt.xlabel('Position')
            plt.ylabel('Reads Mapped')
            plt.title('{}\n'.format(row[0]))
            ax.spines['right'].set_visible(False)  # Removes right axis
            ax.spines['top'].set_visible(False)  # Removes top axis
            ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
            ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top
            plt.savefig('/nethome/mct30/mapping_svgs/{0}_plant-precursors_bowtie1_a_T_merged.svg'.format(row[12]), 
                        bbox_inches = 'tight', format = 'svg')
            plt.show()
            plt.close('all')
        else:
            pass
    
    return mybam_lc


with open('/nethome/mct30/exact_mirs.fa', 'r') as f:
    for name in f:
        name = name.rstrip('\n').lstrip('>')
        names.append(name)
        seq = next(f).rstrip('\n').replace('T', 'U')
        seqs.append(seq)

rows = []
with open('/nethome/mct30/ShortStack-miRBase_37-46_56-58_12_19_m-s-per_len.csv', 'r') as f, \
     open('/nethome/mct30/exact_mirs_precursor_info.csv', 'w', newline = '') as f_write:
    csvreader = csv.reader(f, delimiter = ',')
    csvwriter = csv.writer(f_write)
    header = next(csvreader)
    for row in csvreader:
        mature = row[3]
        star = row[5]
        if mature in seqs:
            name = names[seqs.index(mature)]
#            row[0] = '{0}_{1}'.format(name, row[0])
#            csvwriter.writerow(row)
#            rows.append(row)
            mybam_lc = pull_down(name, row)
        elif star in seqs:
            name = names[seqs.index(star)]
#            row[0] = '{0}_{1}'.format(name, row[0])
#            csvwriter.writerow(row)
#            rows.append(row)
            mybam_lc = pull_down(name, row)
        else:
            pass
        
