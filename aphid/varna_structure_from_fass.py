#import matplotlib
#matplotlib.use('Agg')
import numpy as np
import csv
#import pysam
#import pysamstats
#import matplotlib.pyplot as plt
from subprocess import call

names = []
seqs = []

#mybam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G006_G002_BTIRed_Gut_plant-precursors_bowtie1_a_T.merged.sorted.bam')
#G006_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G006_Gut_plant-precursors_bowtie1_a_T.sorted.bam')
#G002_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/G002_Gut_plant-precursors_bowtie1_a_T.sorted.bam')
#BTIRed_bam = pysam.AlignmentFile('/nethome/mct30/bmds/SAM_out/BTIRed_Gut_plant-precursors_bowtie1_a_T.sorted.bam')

#def pull_down(name, row):
#    row[0] = '{0}_{1}'.format(name, row[0])
#    csvwriter.writerow(row)
#    rows.append(row)
#    chrom = row[0]
#    start = 1
##    chrom = row[12].split(':')[0]
##    start = int(row[12].split(':')[1].split('-')[0])
##    end = int(row[12].split(':')[1].split('-')[1])
#    #row = ['csi-miR395c-3p_Cluster_151156', '86.36', '21', 'CUGAAGUGUUUGGGGGAACUC', '7', 'GUUCCUCUGAGCACUUCAUUG', '6', '21', 'ACUGAAGUGUUUGGGGGAACUCC', 'AGUUCCUCUGAGCACUUCAUUGG', 'UUGGUCGGAUGUCUCCUAGAGUUCCUCUGAGCACUUCAUUGGGUAUACAAUUUCUUAUGAAGAUUACCCACUGAAGUGUUUGGGGGAACUCCUGGACCCAUUCUACGGUUU']
##    mybam_lc = pysamstats.load_coverage(mybam, chrom = chrom, start = start, 
##                                        end = end)
#    mybam_lc = pysamstats.load_coverage(mybam, chrom = chrom)
#    G006_bam_lc = pysamstats.load_coverage(G006_bam, chrom = chrom)
#    G002_bam_lc = pysamstats.load_coverage(G002_bam, chrom = chrom)
#    BTIRed_bam_lc = pysamstats.load_coverage(BTIRed_bam, chrom = chrom)
#    
#    mature = row[3]
#    star = row[5]
#    precursor = row[10]
#    end = len(precursor)
#    if any(m.islower() for m in mature) or any(s.islower() for s in star):
#        pass
#    else:
#        m_start = precursor.index(mature)
#        m_end = m_start + len(mature)
#        s_start = precursor.index(star)
#        s_end = s_start + len(star)
#    
##        if len(mybam_lc.pos) > 0:
#        if (len(G006_bam_lc.pos) > 0) or (len(G002_bam_lc.pos) > 0) or \
#        (len(BTIRed_bam_lc.pos) > 0):
#            positions = np.arange(start, end + 1)
#            read_counts = []
#            
#            G006_bam_lc_pos = list(G006_bam_lc.pos)
#            for entry in positions:
#                if entry in G006_bam_lc_pos:
#                    read_counts.append(G006_bam_lc.reads_all[G006_bam_lc_pos.index(entry)])
#                else:
#                    read_counts.append(0)
#                    
#            G002_bam_lc_pos = list(G002_bam_lc.pos)
#            for entry in positions:
#                if entry in G002_bam_lc_pos:
#                    pos_ind = entry - 1
#                    read_counts[pos_ind] += G002_bam_lc.reads_all[G002_bam_lc_pos.index(entry)]
#                else:
#                    pass
#            
#            BTIRed_bam_lc_pos = list(BTIRed_bam_lc.pos)
#            for entry in positions:
#                if entry in BTIRed_bam_lc_pos:
#                    pos_ind = entry - 1
#                    read_counts[pos_ind] += BTIRed_bam_lc.reads_all[BTIRed_bam_lc_pos.index(entry)]
#                else:
#                    pass
#            
#            print(read_counts)
#            fig = plt.figure(figsize = (15, 15))
#            ax = plt.subplot(1, 1, 1)
##            if m_start > s_start:
##                plt.plot(positions[:s_start], read_counts[:s_start], 
##                         color = 'black', label = 'Tails')
##                plt.plot(positions[s_start:s_end+1], read_counts[s_start:s_end+1], 
##                         color = 'red', label = 'Star')
##                plt.plot(positions[s_end+1:m_start], read_counts[s_end+1:m_start], 
##                         color = 'gold', label = 'Loop')
##                plt.plot(positions[m_start:m_end+1], read_counts[m_start:m_end+1], 
##                         color = 'green', label = 'Mature')
##                plt.plot(positions[m_end+1:], read_counts[m_end+1:], 
##                         color = 'black')
##            elif s_start > m_start:
##                plt.plot(positions[:m_start], read_counts[:m_start], 
##                         color = 'black', label = 'Tails')
##                plt.plot(positions[m_start:m_end+1], read_counts[m_start:m_end+1], 
##                         color = 'green', label = 'Mature')
##                plt.plot(positions[m_end+1:s_start], read_counts[m_end+1:s_start], 
##                         color = 'gold', label = 'Loop')
##                plt.plot(positions[s_start:s_end+1], read_counts[s_start:s_end+1], 
##                         color = 'red', label = 'Star')
##                plt.plot(positions[s_end+1:], read_counts[s_end+1:], 
##                         color = 'black')
#            barlist = plt.bar(positions, read_counts, width = 1.0, 
#                              color = 'black')
#            for bar in barlist[m_start:m_end + 1]:
#                bar.set_color('red')
#            for bar in barlist[s_start:s_end + 1]:
#                bar.set_color('green')
#            if m_start > s_start:
#                for bar in barlist[s_end + 1:m_start]:
#                    bar.set_color('yellow')
#            elif s_start > m_start:
#                for bar in barlist[m_end + 1:s_start]:
#                    bar.set_color('yellow')
#            else:
#                pass
##            plt.legend()
#            ind = np.arange(max(read_counts) + 1)
#            plt.yticks(ind, ind)
#            plt.xlabel('Position')
#            plt.ylabel('Reads Mapped')
#            plt.title('{}\n'.format(row[0]))
#            ax.spines['right'].set_visible(False)  # Removes right axis
#            ax.spines['top'].set_visible(False)  # Removes top axis
#            ax.yaxis.set_ticks_position('none')  # Keeps vertical ticks hidden
#            ax.xaxis.set_ticks_position('bottom')  # Keeps horizontal ticks hidden on top
#            plt.savefig('/nethome/mct30/mapping_svgs/{0}_plant-precursors_bowtie1_a_T_merged.svg'.format(row[12]), 
#                        bbox_inches = 'tight', format = 'svg')
#            plt.show()
#            plt.close('all')
#        else:
#            pass
##    read_counts[m_start : m_end + 1]
#    return mybam_lc

def VARNA_fig(name, row, struct):
    title = '{0} ({1})'.format(name.replace('/', ','), row[0])
    name = '{0}_{1}'.format(name.replace('/', ','), row[0])
    mature = row[3]
    star = row[5]
    precursor = row[10]
    seq = precursor
    end = len(precursor)
    if any(m.islower() for m in mature) or any(s.islower() for s in star):
        pass
    else:
        m_start = precursor.index(mature)
        m_end = m_start + len(mature)
        s_start = precursor.index(star)
        s_end = s_start + len(star)
        mir_place = round(((m_end - m_start)/2), 0)
        mir_s_place = round((s_end - s_start)/2)
        m_start = m_start + 1
        s_start = s_start + 1
        if m_start > s_start:
            call(['java', '-cp', '/home/underasail/scripts/VARNAv3-93.jar', 
                  'fr.orsay.lri.varna.applications.VARNAcmd', 
                  '-annotations', 'M:type=B,size=24,color=#000000,anchor='+str(int(mir_place) + m_start)
                  +';*:type=B,size=24,color=#000000,anchor='+str(int(mir_s_place) + s_start), 
                  '-title', title, '-titlesize', '12', 
                  '-sequenceDBN', seq, 
                  '-structureDBN', struct, 
                  '-highlightRegion', str(m_start)+'-'+str(m_end)+':radius=16,fill=#BCFFDD,outline=#6ED86E;'
                  +str(s_start)+'-'+str(s_end)+':radius=16,fill=#FF9999,outline=#FF3333;'
                  +str(s_end + 1)+'-'+str(m_start - 1)+':radius=16,fill=#FFF1A6,outline=#FFD700', 
                  '-o', name + '_plant-precursors_structure_RNAfold.png'])
        elif s_start > m_start:
            call(['java', '-cp', '/home/underasail/scripts/VARNAv3-93.jar', 
                  'fr.orsay.lri.varna.applications.VARNAcmd', 
                  '-annotations', 'M:type=B,size=24,color=#000000,anchor='+str(int(mir_place) + m_start)
                  +';*:type=B,size=24,color=#000000,anchor='+str(int(mir_s_place) + s_start), 
                  '-title', title, '-titlesize', '12', 
                  '-sequenceDBN', seq, 
                  '-structureDBN', struct, 
                  '-highlightRegion', str(m_start)+'-'+str(m_end)+':radius=16,fill=#BCFFDD,outline=#6ED86E;'
                  +str(s_start)+'-'+str(s_end)+':radius=16,fill=#FF9999,outline=#FF3333;'
                  +str(m_end + 1)+'-'+str(s_start - 1)+':radius=16,fill=#FFF1A6,outline=#FFD700', 
                  '-o', name + '_plant-precursors_structure_RNAfold.png'])
        else:
            pass
    
    return title

with open('/home/underasail/Thompson/Documents/exact_mirs_wo-old.fa', 'r') as f:
    for name in f:
        name = name.rstrip('\n').lstrip('>')
        names.append(name)
        seq = next(f).rstrip('\n').replace('T', 'U')
        seqs.append(seq)

struct_names = []
structs = []
with open('/home/underasail/Thompson/Documents/exact_mirs_precursors_T_new.fass', 'r') as f:
    for name in f:
        name = name.rstrip('\n').lstrip('>')  #.split('_')[0]
        seq = next(f).rstrip('\n').replace('T', 'U')
        struct = next(f).rstrip('\n')
        struct_names.append(name)
        structs.append(struct)

rows = []
with open('/home/underasail/Thompson/Documents/ShortStack-miRBase_37-46_56-58_12_19_m-s-per_len.csv', 'r') as f:  #, \
#     open('/nethome/mct30/exact_mirs_precursor_info.csv', 'w', newline = '') as f_write:
    csvreader = csv.reader(f, delimiter = ',')
#    csvwriter = csv.writer(f_write)
    header = next(csvreader)
    for row in csvreader:
        mature = row[3]
        star = row[5]
        if mature in seqs:
            seqs_ind = seqs.index(mature)
            name = names[seqs_ind]
#            mybam_lc = pull_down(name, row)
            
            struct_name = '{0}_{1}'.format(name, row[0])
            struct_ind = struct_names.index(struct_name)
            struct = structs[struct_ind]
            title = VARNA_fig(name, row, struct)
        elif star in seqs:
            seqs_ind = seqs.index(star)
            name = names[seqs_ind]
#            mybam_lc = pull_down(name, row)
            
            struct_name = '{0}_{1}'.format(name, row[0])
            struct_ind = struct_names.index(struct_name)
            struct = structs[struct_ind]
            title = VARNA_fig(name, row, struct)
        else:
            pass
        
