#! /usr/bin/python

from sys import argv
import csv
from subprocess import call

title_dict = {}

# argv[1]: ./miR-PREFeR_predictions/_miRNA.precursor.ss
#     (should be filtered to include only >=75% 1nt variants
with open(argv[1]) as f:
    csvreader = csv.reader(f, delimiter = ' ')
    for row in csvreader:
#        if row[2] == row[4]:
#            title = row[2]
#        else:
#            title = '-'.join(row[2:])
        title = '-'.join(row[2:])
        print(title)
        title = title.lstrip('miRNA-')
        seq = next(csvreader)[0]
        struct = next(csvreader)[0]
        mirstrand = next(csvreader)[0]
        for i, char in enumerate(mirstrand):
            if char == 'M' and mirstrand[i-1] == '.':
                M_start = i+1
                # plus one positions correctly for VARNA but is ahead on in normal
            elif char == 'M' and i + 1 == len(mirstrand):
                # allows the mature strand to end without a tail
                M_end = i+1
            elif char == 'M' and mirstrand[i+1] == '.':
                M_end = i+1
            elif char == 'S' and mirstrand[i-1] == '.':
                S_start = i+1
            elif char == 'S' and i + 1 == len(mirstrand):
                # allows the star strand to end without a tail
                S_end = i+1
            elif char == 'S' and mirstrand[i+1] == '.':
                S_end = i+1
            else:
                pass
        mir_place = round(((M_end - M_start)/2), 0)
        mir_s_place = round((S_end - S_start)/2)
        # print('<(echo -e ">%s\n%s")' % (title, seq[(M_start-1):(M_end-1)]))
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
        # call(['blastn', '-query', '<(echo -e ">%s\n%s")' % (title, seq[(M_start-1):(M_end-1)]), '-db', 
        #       '/home/underasail/blastdbs/miRBase_mature', '-task', 'blastn-short', '-word_size', '4', 
        #       '-dust', 'no', '-soft_masking', 'false', '-num_alignments', '2', '-num_descriptions', '2', 
        #       '-out', '/home/underasail/%s_miRBase_mature.out' % title])

