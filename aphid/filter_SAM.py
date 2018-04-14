#! /share/opt/python/3.6.5/bin/python3

from sys import argv
import csv

seq_dict = {}
aphid_seq_dict = {}
buchnera_seq_dict = {}
plant_seq_dict = {}

with open(argv[1], newline='') as f:
    aphid_csv = csv.reader(f, delimiter = '\t')
    for row in aphid_csv:
        readnum = row[0]
        seq = row[9]
        if ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            seq_dict.setdefault(seq, []).append('aphid_%s' % readnum)

with open(argv[2], newline='') as f:
    buchnera_csv = csv.reader(f, delimiter = '\t')
    for row in buchnera_csv:
        readnum = row[0]
        seq = row[9]
        if ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            seq_dict.setdefault(seq, []).append('buchnera_%s' % readnum)

with open(argv[3], newline='') as f:
    plant_csv = csv.reader(f, delimiter = '\t')
    for row in plant_csv:
        readnum = row[0]
        seq = row[9]
        if ('XM:i:0' in str(row) or 'XM:i:1' in str(row)):
            seq_dict.setdefault(seq, []).append('plant_%s' % readnum)

for seq, readnum in seq_dict.items():
    if len(seq_dict[seq]) > 1:
        pass
    else:
        if 'aphid' in readnum[0]:
            aphid_seq_dict.setdefault(seq, []).append(readnum)
        elif 'buchnera' in readnum[0]:
            buchnera_seq_dict.setdefault(seq, []).append(readnum)
        elif 'plant' in readnum[0]:
            plant_seq_dict.setdefault(seq, []).append(readnum)
        else:
            print('Error')

with open(argv[1], newline='') as fr:
    aphid_csv = csv.reader(fr, delimiter = '\t')
    with open(argv[4], 'w', newline='') as fw:
        aphid_csv_writer = csv.writer(fw, delimiter = '\t')
        for row in aphid_csv:
            readnum = row[0]
            seq = row[9]
            try:
                e = aphid_seq_dict[seq]
                aphid_csv_writer.writerow(row)                    
            except KeyError:
                pass

with open(argv[2], newline='') as fr:
    buchnera_csv = csv.reader(fr, delimiter = '\t')
    with open(argv[5], 'w', newline='') as fw:
        buchnera_csv_writer = csv.writer(fw, delimiter = '\t')
        for row in buchnera_csv:
            readnum = row[0]
            seq = row[9]
            try:
                e = buchnera_seq_dict[seq]
                buchnera_csv_writer.writerow(row)
            except KeyError:
                pass

with open(argv[3], newline='') as fr:
    plant_csv = csv.reader(fr, delimiter = '\t')
    with open(argv[6], 'w', newline='') as fw:
        plant_csv_writer = csv.writer(fw, delimiter = '\t')
        for row in plant_csv:
            readnum = row[0]
            seq = row[9]
            try:
                e = plant_seq_dict[seq]
                plant_csv_writer.writerow(row)
            except KeyError:
                pass
