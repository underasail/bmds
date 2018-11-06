#! /share/opt/python/3.6.5/bin/python

import csv

scores_dict = {}

with open('G006_Gut_F_trimmed_17-35_plants_miRNA.mature_unique_targets_pita_results_targets.tab') as f:
    csvreader = csv.reader(f, delimiter = "\t")
    header = next(csvreader)
    for row in csvreader:
        if float(row[3]) <= -10:
            scores_dict.setdefault(row[1], []).append(row)
for key in scores_dict.keys():
    print('%s: %s' % (key, len(scores_dict[key])))