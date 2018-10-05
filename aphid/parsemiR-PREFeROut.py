#! /usr/bin/python

import csv
from subprocess import call

title_dict = {}

with open('/home/underasail/Thompson/Documents/G006_Gut_F_trimmed_17-35_plants_miRNA.precursor.ss', 'r') as f:
    csvreader = csv.reader(f, delimiter = ' ')
    for row in csvreader:
        title = row[2]
        # title = row[0] + row[1] + row[2]
        title = title.lstrip('miRNA-')
        seq = next(csvreader)[0]
        struct = next(csvreader)[0]
        mirstrand = next(csvreader)[0]
        for i, char in enumerate(mirstrand):
            if char == 'M' and mirstrand[i-1] == '.':
                M_start = i+1
            elif char == 'M' and mirstrand[i+1] == '.':
                M_end = i+1
            elif char == 'S' and mirstrand[i-1] == '.':
                S_start = i+1
            elif char == 'S' and i + 1 == len(mirstrand):
                S_end = i+1
            elif char == 'S' and mirstrand[i+1] == '.':
                S_end = i+1
            else:
                pass
        mir_place = round(((M_end - M_start)/2), 0)
        mir_s_place = round((S_end - S_start)/2)
        call(['java', '-cp', '/home/underasail/scripts/VARNAv3-93.jar', 
              'fr.orsay.lri.varna.applications.VARNAcmd', 
              '-annotations', 'M:type=B,size=24,color=#000000,anchor='+str(int(mir_place) + M_start)
              +';*:type=B,size=24,color=#000000,anchor='+str(int(mir_s_place) + S_start), 
              '-title', title, '-titlesize', '24', 
              '-sequenceDBN', seq, 
              '-structureDBN', struct, 
              '-highlightRegion', str(M_start)+'-'+str(M_end)+':radius=16,fill=#BCFFDD,outline=#6ED86E;'
              +str(S_start)+'-'+str(S_end)+':radius=16,fill=#FF9999,outline=#FF3333', 
              '-o', title + '.svg'])

