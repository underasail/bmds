#! /usr/bin/python

#from sys import argv
import csv

strand_list = []
ps_list = []
tf_list = []
total_list = []
p_dict = {}
t_dict = {}

with open('psRNATargetJob-s4fer50.9nomismatchinseed.out') as f:  # psRNAtarget
    csvreader = csv.reader(f, delimiter = '\t')
    warning = next(csvreader)
    header = next(csvreader)
    for row in csvreader:
        start = int(row[6])
        end = int(row[7])
        mirna = row[0]
        target = row[1]
        ps_list.append([mirna+'\t'+target, set(list(range(start, end)))])
        p_dict.setdefault(mirna+'\t'+target, []).append(set(list(range(start, end))))
        

with open('exact_mirs_targetfinder_cat.out') as f:  # RNAhybrid
    csvreader = csv.reader(f, delimiter = '\t')
    header = next(csvreader)
    for row in csvreader:
        mirna = row[0]
        target = row[1].split(' ')[0]
        start = int(row[2])
        end = int(row[3])
        tf_list.append([mirna+'\t'+target, set(list(range(start, end)))])
        t_dict.setdefault(mirna+'\t'+target, []).append(set(list(range(start, end))))

p_set = set()
t_set = set()
for p in ps_list:
    p_set.add(p[0])
for t in tf_list:
    t_set.add(t[0])
total_set = p_set & t_set

#strand_dict = {}
#
#for entry in strand_list:
#    if '%s\t%s' % (entry.split('\t')[0], entry.split('\t')[1]) in total_set:
#        strand_dict.setdefault('%s\t%s' % (entry.split('\t')[0], entry.split('\t')[1]), []).append(entry.split('\t')[2])
#    else:
#        pass

for entry in total_set:
    if len(p_dict[entry]) > 1 or len(t_dict[entry]) > 1:
        b = set()
        for value in p_dict[entry]:
            b = b | value
            p_dict[entry] = b
        b = set()
        for value in t_dict[entry]:
            b = b | value
            t_dict[entry] = b
        if len(set(p_dict[entry] & t_dict[entry])) > 0:
            seed = sorted(set(p_dict[entry] & t_dict[entry]))
            if (1 + seed[-1] - seed[0]) > 8:
                print('ERROR: Fix entry below manually')
                print(seed)
#                print(entry+'\t'+str(seed[0])+'\t'+str(seed[-1])+'\t'+strand_dict[entry][0])
                print(entry+'\t'+str(seed[0])+'\t'+str(seed[-1]))
            else:
#                print(entry+'\t'+str(seed[0])+'\t'+str(seed[-1])+'\t'+strand_dict[entry][0])
                print(entry+'\t'+str(seed[0])+'\t'+str(seed[-1]))
    else:
        if len(set(p_dict[entry][0] & t_dict[entry][0])) > 0:
            seed = sorted(set(p_dict[entry][0] & t_dict[entry][0]))
            print(entry+'\t'+str(seed[0])+'\t'+str(seed[-1]))


