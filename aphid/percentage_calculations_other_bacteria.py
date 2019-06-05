
# USAGE: ./percentage_calculations.py [APHID SAM FILE] [BUCHNERA SAM FILE] [PLANT SAM FILE] [OTHER BACT SAM FILE] [PERCENTAGE OUTPUT]

from sys import argv
import csv
from Bio import Entrez
from Bio import SeqIO
import pickle

#argv = ['percentage_calculations_other_bacteria.py', 'C:\\Users\\Thompson\\Downloads\\G006_Gut_Myzus-only.map', 'C:\\Users\\Thompson\\Downloads\\G006_Gut_Buchnera-only.map', 'C:\\Users\\Thompson\\Downloads\\G006_Gut_plants-only.map', 'C:\\Users\\Thompson\\Downloads\\G006_Gut_other-bacteria_full-alignment.map', 'C:\\Users\\Thompson\\Documents\\G006_Gut_other_bacteria_percentages.txt']

Entrez.email = 'mct30@miami.edu'

matched_dict = {}
genomes_dict = {}
aphid = set()
buchnera = set()
plant = set()
ob = set()
Ps = set()
CRi = set()

primary = ['Buchnera', 'Myzus']
secondary = ['plants', 'other_bacteria', 'viruses']
genomes_dict = {}

if 'G002' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 3427212
        elif any(word in argv[1] for word in primary):
            totalreads = 12085742
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 5942393
        elif any(word in argv[1] for word in primary):
            totalreads = 9032198
elif 'G006' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 2054109
        elif any(word in argv[1] for word in primary):
            totalreads = 21960873
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 1530897
        elif any(word in argv[1] for word in primary):
            totalreads = 2626650
elif 'BTIRed' in argv[1]:
    if 'Bac' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 3999644
        elif any(word in argv[1] for word in primary):
            totalreads = 13931847
    elif 'Gut' in argv[1]:
        if any(word in argv[1] for word in secondary):
            totalreads = 6570398
        elif any(word in argv[1] for word in primary):
            totalreads = 9064708


with open(argv[1], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
            refgen = 'aphid'
            aphid.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
        else:
            pass

with open(argv[2], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            refgen = 'buchnera'
            buchnera.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
        else:
            pass

with open(argv[3], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            refgen = 'plant'
            plant.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
        else:
            pass

mapped_to_a_b_p = aphid | buchnera | plant

with open(argv[4], newline='') as f:
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if (len(row) >= 14) and ('XM:i:0' or 'XM:i:1' in str(row)):
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            if readnum not in mapped_to_a_b_p:
                genomes_dict.setdefault(refgen, []).append(readnum)
            else:
                pass
            if 'AE016853.1' == refgen:
                Ps.add(readnum)
            elif 'NZ_AGCA01000390.1' == refgen:
                CRi.add(readnum)
            else:
                refgen = 'ob'
                ob.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
        else:
            pass

ob_ex = ob - aphid - buchnera - plant
Ps_ex = Ps - CRi - ob - aphid - buchnera - plant
CRi_ex = CRi - Ps - ob - aphid - buchnera - plant

#with open(argv[5], 'w') as f:
#    f.write('Total: {}\n'.format((len(aphid | buchnera | plant | ob)/totalreads)*100))
#    #print('All: ', len(aphid & buchnera & plant))
#    #print('Aphid and plant: ', len((aphid & plant) - buchnera))
#    #print('Aphid and Buchnera: ', len((aphid & buchnera) - plant))
#    #print('Buchnera and Plant: ', len((buchnera & plant) - aphid))
#    #print('Aphid: ', len(aphid - buchnera - plant))
#    #print('Buchnera: ', len(buchnera - aphid - plant))
#    #print('Plant: ', len(plant - aphid - buchnera))
#    f.write('Other Bacteria: {}\n'.format((len(ob - plant - aphid - buchnera)/totalreads)*100))
#%%
#genbank_accession_numbers = list(genomes_dict.keys())
#efetch_handle = Entrez.efetch(db = 'nuccore', id = genbank_accession_numbers, rettype = 'gb', retmode = 'text')
#efetch_records = SeqIO.parse(efetch_handle, 'gb')
## Search all accession numbers at once to avoid API search limits at NCBI
#for (record, genbank_accession_number) in zip(efetch_records, genbank_accession_numbers):
#    organism_name = record.annotations['organism']
#    record_GBA = str(record.annotations['accessions'][0])
#    if record_GBA in str(genbank_accession_number):
#        genomes_dict[organism_name] = genomes_dict.pop(genbank_accession_number)
#    else:
#        print('Records not aligned')
#    # Pulls the organism name from the annotations of the SeqRecord
#    # object to identify the genome later on in output files
#    genomes_dict[organism_name].append(record.description)
#    # Added description to end of readnums list because it contains strain 
#    # and genome info
#    print(organism_name)

with open('/nethome/mct30/bmds/org_names.pkl', 'rb') as list_file:
#with open('org_names.pkl', 'rb') as list_file:
    org_names = pickle.load(list_file)

for org_set in org_names:
    name = org_set[0]
    accession = org_set[1]
    description = org_set[2]
    try:
        description = description[:description.index(',')]
    except ValueError:
        description = description[:description.index(' complete')]
    try:
        genomes_dict[description] = genomes_dict.pop(accession)
    except KeyError:
        pass

ordered_list = sorted(genomes_dict, key=lambda x: (len(genomes_dict[x]), x), reverse = True)

with open(argv[5], 'w') as f:
#    f.write('{}\t\t\t\n'.format(argv[1]))
    f.write('{}\t\t\n'.format(argv[1]))
    f.write('Total: {}%\n'.format(round((len(aphid | buchnera | plant | ob)/totalreads)*100, 2)))
    f.write('Other Bacteria Exclusively (without Ps or CRi): {0}%\t{1}\n'.format(round((len(ob_ex)/totalreads)*100, 2), len(ob_ex)))
    f.write('Pseudomonas syringae pv. tomato str. DC3000 Exclusively: {0}%\t{1}\n'.format(round((len(Ps_ex)/totalreads)*100, 2), len(Ps_ex)))
    f.write('Candidatus Regiella insecticola 5.15 Rin_2504559902.53 Exclusively: {0}%\t{1}\n'.format(round((len(CRi_ex)/totalreads)*100, 2), len(CRi_ex)))
#    f.write('Percentage\tNumber of Reads\tOrganism Name\tDescription\n')
    f.write('Percentage\tNumber of Reads\tOrganism Name\n')
    for entry in ordered_list:
        readnums = genomes_dict[entry]
        refgen = entry
#        count = len(readnums) - 1
#        # -1 accounts for added description at the end
        count = len(readnums)
        genomes_dict[refgen].append(count)
        # Appends a new entry to end of readnums list with
        # the number of matched reads for that genome
        percent = round(((count/totalreads)*100), 4)
        # Calculates the percent of total reads mapped to that ggenome
        genomes_dict[refgen].append(percent)
        # genomes_dict[genome] = {read1, read2, ... , count, percentage}
#        f.write('%s%%\t%s\t%s\t%s\n' % (percent, count, refgen, readnums[-3]))
        f.write('{0}%\t{1}\t{2}\n'.format(percent, count, refgen))

