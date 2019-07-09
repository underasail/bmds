
import csv

seqs = []
structs = []

with open('exact_mirs_precursors_T.fass', 'r') as f:
    for line in f:
        name = line
        seq = next(f).rstrip('\n')
        seqs.append(seq)
        struct = next(f).rstrip('\n')
        structs.append(struct)

with open('exact_mirs_precursor_info.csv', 'r') as f, open('exact_mirs_precursors_T_new.fass', 'w') as f_write:
    csvreader = csv.reader(f, delimiter = ',')
    for row in csvreader:
        name = row[0]
        seq = row[10]  # .replace('U', 'T')
        struct = row[11]
        if seq in seqs:
            f_write.write(">{0}\n{1}\n{2}\n".format(name, seq, struct))
        else:
            pass
     
#%%