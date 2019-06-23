from os import listdir
import csv
import re
import matplotlib.pyplot as plt

map_folder = 'C:\\Users\\Thompson\\AppData\\Local\\Packages\\CanonicalGroupLimited.'\
              'UbuntuonWindows_79rhkp1fndgsc\\LocalState\\rootfs\\home\\underasail\\mapping_svgs\\'

txt_files = []
map_folder_files = listdir(map_folder)
for file in map_folder_files:
    if file.endswith('_reads.txt') and file not in ['summary_reads.txt', 'sbi-miR156e_Cluster_177978_reads.txt', 'aof-miR156a_Cluster_1224_reads.txt', 'aof-miR168a_Cluster_233394_reads.txt']:
        txt_files.append(file)
    else:
        pass

#txt_files = ['mtr-miR169i-1_Cluster_190553_reads.txt']
#txt_files = ['fve-miR162-3p_Cluster_32077_reads.txt']
#txt_files = ['csi-miR168-3p_Cluster_2535_reads.txt']
#txt_files = ['aly-miR393b-3p_Cluster_134074_reads.txt']

for file in txt_files:
    with open(map_folder + file) as f:
        csvreader = csv.reader(f, delimiter = ' ')
        name = next(csvreader)[0]
        precursor = ref_seq = next(csvreader)[0].replace('U', 'T')
        mature = re.split(r'([AGCTU]+)', next(csvreader)[0])[1]
        star = re.split(r'([AGCTU]+)', next(csvreader)[0])[1]
        empty = next(csvreader)
        reads_aligned = next(csvreader)
        
        m_start = precursor.index(mature)
        m_end = m_start + len(mature)
        s_start = precursor.index(star)
        s_end = s_start + len(star)
        end = len(precursor)
        
        read_seqs = []
        read_counts = []
        reads_expanded = []
        for row in csvreader:
            if row[0][0] == '.':
                read_seq = re.split(r'([AGCTU]+)', row[0])[1]
                read_count = int(row[1])
                read_seqs.append(read_seq)
                read_counts.append(read_count)
                reads_expanded += [read_seq] * read_count

#%%
        inds = []
        inds_2 = []
        lines = []
        a_ind = 0
        a = []
        for read in reads_expanded:
            start_ind = ref_seq.index(read)
            end_ind = start_ind + len(read)
            inds.append([start_ind, end_ind, read])
        len_inds = len(inds)
        while len(inds_2) < len_inds:
            line = []
            split_list = list(zip(*inds))

            first_line_entry = inds[split_list[1].index(min(split_list[1]))]
            line.append(first_line_entry)
            last_entry_index = inds.index(line[-1])
            inds = inds[:last_entry_index] + inds[last_entry_index + 1:]
            split_list = list(zip(*inds))
            if len(split_list) == 0:
                break
            else:
                pass
            while any(split_list[0][j] > (line[-1][1] + 1) for j in range(0, len(split_list[0]))):
                a = []
                for entry in inds:
                    if entry[0] > (1 + line[-1][1]):
                        a.append(entry)
                    else:
                        pass
                if len(a) > 0:
                    a = list(zip(*a))
                    a_ind = a[1].index(min(a[1]))
                    line_entry = [a[0][a_ind], a[1][a_ind], a[2][a_ind]]
                    line.append(line_entry)
                    last_entry_index = inds.index(line[-1])
                    inds = inds[:last_entry_index] + inds[last_entry_index + 1:]
                    split_list = list(zip(*inds))
                else:
                    pass
                if len(split_list) == 0:
                    break
                else:
                    pass

            for entry in line:
                inds_2.append(entry)
            lines.append(line)
            if len(split_list) == 0:
                break
            else:
                pass
            
#%%
        fig = plt.figure(figsize = (15, 7))
        ax = plt.subplot(1, 1, 1)
        i = 0
        for line in lines:
            i += 1
            for entry in line:
                x = list(range(entry[0], entry[1] + 1))
                y = [i] * len(x)
                plt.plot(x, y, color = 'black', linewidth = 5)

#%%

#        reads = 0
#        i = 0
#        j = 0
#        bottom_read_x = last_read_x = [0]
#        js = []
#        xs = []
#        last_j = 0
#        j_dict = {}
#        num2 = 0
#        for num1 in range(0, 1501):
#            j_dict[num1] = []
#        for read_seq, read_count in zip(read_seqs, read_counts):
#            i += 1
#            ref_seq_index = ref_seq.index(read_seq)
#            x = list(range(ref_seq_index + 1, ref_seq_index + len(read_seq) + 1))
#            k = 0
#            if j not in [0, 1]:
#                for num in range(1, j + 1):
#                    try:
#                        next_ref_seq_index = ref_seq.index(reads_expanded[reads + num - 1])
#                        x_range = list(range(next_ref_seq_index + 1, next_ref_seq_index + len(reads_expanded[i + num]) + 1))
#                        if min(x_range) >= (max(j_dict[num]) + 2) and \
#                        min(j_dict[num]) > 0:
##                            print(j, num, max(j_dict[num]), min(x_range))
#                            k = num
#                        else:
##                            print(j, num, max(j_dict[num]), min(x_range), 'Failed')
#                            break
#                    except IndexError:
##                        print('IndexError')
#                        break
#                if k >= j or k == len(reads_expanded) - reads:
##                    print('yes')
#                    j = 0
#                elif k < j and 0 < k <= read_count:
#                    j_standin = j
#                    j = 0
#                    reads += k
#                    read_count = read_count - k
#                    for j in range(j + 1, k + 1 + j):
##                        print('\n', j, min(x))
#                        y = [j] * (len(read_seq))
#                        plt.plot(x, y, color = 'black')
#                        j_dict.setdefault(j, []).extend(x)
#                    js.append(j)
#                    prev_j = j
#                    j = j_standin
##                elif k >= prev_j:
##                    print('Happened')
##                    j_standin = j
##                    j = prev_j
##                    reads += read_count
###                    read_count = read_count - k
##                    for j in range(j + 1, read_count + 1 + j):
##                        print('\n', j, min(x))
##                        y = [j] * (len(read_seq))
##                        plt.plot(x, y, color = 'black')
##                        j_dict.setdefault(j, []).extend(x)
##                    js.append(j)
###                    prev_j = j
##                    j = j_standin
#                else:
#                    pass
#            else:
#                pass
#            reads += read_count
#            for j in range(j + 1, read_count + 1 + j):
##                print('\n', j, min(x))
#                y = [j] * (len(read_seq))
#                plt.plot(x, y, color = 'black')
#                j_dict.setdefault(j, []).extend(x)
#            js.append(j)
##            j += 1

#%%

    if m_start > s_start:
        plt.axvspan(0, s_start + 0.5, color = 'black', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(s_start + 0.5, s_end + 0.5, color = 'firebrick', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(s_end + 0.5, m_start + 0.5, color = 'gold', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(m_start + 0.5, m_end + 0.5, color = 'darkgreen', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(m_end + 0.5, end, color = 'black', 
                    alpha = 0.25, zorder = 1)
    elif s_start > m_start:
        plt.axvspan(0, m_start + 0.5, color = 'black', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(m_start + 0.5, m_end + 0.5, color = 'darkgreen', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(m_end + 0.5, s_start + 0.5, color = 'gold', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(s_start + 0.5, s_end + 0.5, color = 'firebrick', 
                    alpha = 0.25, zorder = 1)
        plt.axvspan(s_end + 0.5, end, color = 'black', 
                    alpha = 0.25, zorder = 1)
    plt.xlim(0, len(ref_seq))
#    plt.ylim(0.75, max(js) + 0.5)
    plt.ylim(0.25, i + 0.75)
    plt.yticks([], [])
    plt.xlabel('\nPosition in Precursor')
#    plt.ylabel('Reads Mapped\n')
    plt.title('{}\n'.format(name))
    
    fig.set_size_inches(15, 0.25 * i)
    
    if len(reads_expanded) > 50:
        plt.savefig(map_folder + '{0}_individual-reads.svg'.format(name), 
                    bbox_inches = 'tight', format = 'svg')
    else:
        plt.savefig(map_folder + '{0}_individual-reads.svg'.format(name), 
                    bbox_inches = 'tight', format = 'svg')
#        plt.show()
    plt.show()
    plt.close('all')