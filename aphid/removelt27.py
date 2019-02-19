

import csv


with open('G006_G002_BTIRed_Gut_trimmed_17-35_plants.fasta', 'r') as r, open('G006_G002_BTIRed_Gut_trimmed_17-35_plants_lt27.fasta', 'w') as w:
    csvreader = csv.reader(r)
    for row in csvreader:
        header = row[0]
        seq = next(csvreader)[0]
        if len(seq) > 15 and len(seq) < 27:
            w.write(header + '\n')
            w.write(seq + '\n')