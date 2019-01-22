#! /share/opt/python/3.6.5/bin/python

import csv

scores_dict = {}

with open('/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/target_prediction/pita/G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique_targets_pita_results.tab') as f:
    csvreader = csv.reader(f, delimiter = "\t")
    header = next(csvreader)
    for row in csvreader:
        if float(row[12]) <= 0:
            scores_dict.setdefault(row[1], []).append(row)
for key in scores_dict.keys():
    print('%s: %s' % (key, len(scores_dict[key])))
