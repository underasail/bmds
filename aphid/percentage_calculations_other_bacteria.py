
# USAGE: ./percentage_calculations.py [APHID SAM FILE] [BUCHNERA SAM FILE] [PLANT SAM FILE] [OTHER BACT SAM FILE] [PERCENTAGE OUTPUT]

from sys import argv
import csv
from Bio import Entrez
from Bio import SeqIO
import pickle

# argv = ['percentage_calculations_other_bacteria.py', 
#         'C:\\Users\\Thompson\\Downloads\\G006_Gut_Myzus-only.map', 
#         'C:\\Users\\Thompson\\Downloads\\G006_Gut_Buchnera-only.map', 
#         'C:\\Users\\Thompson\\Downloads\\G006_Gut_plants-only.map', 
#         'C:\\Users\\Thompson\\Downloads\\G006_Gut_other_bacteria_HF_2018_corrected.map', 
#         'C:\\Users\\Thompson\\Documents\\G006_Gut_other_bacteria_percentages_HF_2018_corrected.txt']

Entrez.email = 'mct30@miami.edu'

matched_dict = {}
genomes_dict = {}
aphid = set()
buchnera = set()
plant = set()
ob = set()
Ps = set()
CRi = set()
Cn = set()
Pd = set()
Hd = set()
Ss = set()
Ph = set()
Al = set()
Pa = set()
Ea = set()

primary = ['Buchnera', 'Myzus']
secondary = ['plants', 'other_bacteria', 'viruses']
genomes_dict = {}
genomes_dict_collapsed = {}
CRi_rin_list = []
Ps_list = []
Cn_list = []
Pd_list = []
Hd_list = []
Ss_list = []
Ph_list = []
Al_list = []
Pa_list = []
Ea_list = []

with open('/nethome/mct30/bmds/viruses2_org_names.pkl', 'rb') as list_file:
# with open('/nethome/mct30/bmds/org_names.pkl', 'rb') as list_file:
#with open('org_names.pkl', 'rb') as list_file:
    org_names = pickle.load(list_file)

for entry in org_names:
    name = entry[0]
    acc = entry[1]
    if 'Candidatus Regiella insecticola 5.15' in name:
        CRi_rin_list.append(acc)
    elif 'Pseudomonas syringae pv. tomato str. DC3000' in name:
        Ps_list.append(acc)
    elif 'Cupriavidus necator N-1' in name:
        Cn_list.append(acc)
    elif 'Paenibacillus daejeonensis DSM 15491' in name:
        Pd_list.append(acc)
    elif 'Candidatus Hamiltonella defensa' in name:
        Hd_list.append(acc)
    elif 'Serratia symbiotica' in name:
        Ss_list.append(acc)
    elif 'Paenibacillus herberti' in name:
        Ph_list.append(acc)
    elif 'Candidatus Arsenophonus lipoptenae' in name:
        Al_list.append(acc)
    elif 'Pseudomonas aeruginosa PAO1' in name:
        Pa_list.append(acc)
    elif 'Erwinia aphidicola' in name:
        Ea_list.append(acc)
    else:
        pass


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
        if (len(row) >= 14) and (('XM:i:0' or 'XM:i:1') in str(row)):
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
        if (len(row) >= 14) and (('XM:i:0' or 'XM:i:1') in str(row)):
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
        if (len(row) >= 14) and (('XM:i:0' or 'XM:i:1') in str(row)):
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
        if (len(row) >= 14) and (('XM:i:0' or 'XM:i:1') in str(row)):
            readnum = row[0]
            refgen = row[2]
            seq = row[9]
            if readnum not in mapped_to_a_b_p:
                genomes_dict.setdefault(refgen, []).append(readnum)
            else:
                pass
            if refgen in Ps_list:
                Ps.add(readnum)
            elif refgen in CRi_rin_list:
                CRi.add(readnum)
            elif refgen in Cn_list:
                Cn.add(readnum)
            elif refgen in Pd_list:
                Pd.add(readnum)
            elif refgen in Hd_list:
                Hd.add(readnum)
            elif refgen in Ss_list:
                Ss.add(readnum)
            elif refgen in Ph_list:
                Ph.add(readnum)
            elif refgen in Al_list:
                Al.add(readnum)
            elif refgen in Pa_list:
                Pa.add(readnum)
            elif refgen in Ea_list:
                Ea.add(readnum)
            else:
                refgen = 'ob'
                ob.add(readnum)
            matched_dict.setdefault(readnum, []).append(refgen)
        else:
            pass

ob_ex = ob - mapped_to_a_b_p

#if 'G006' in argv[1]:
#    ob_ex = ob_ex | Ps | Cn | Pd
#    CRi_ex = CRi - ob_ex - mapped_to_a_b_p
#elif 'G002' in argv[1]:
#    ob_ex = ob_ex | Pd
#    CRi_ex = CRi - ob_ex - Ps - Cn - mapped_to_a_b_p
#    Ps_ex = Ps - ob_ex - CRi - Cn - mapped_to_a_b_p
#    Cn_ex = Cn - ob_ex - CRi - Ps - mapped_to_a_b_p
#elif 'BTIRed_Gut' in argv[1]:
#    ob_ex = ob_ex | Pd
#    CRi_ex = CRi - ob_ex - Ps - Cn - mapped_to_a_b_p
#    Ps_ex = Ps - ob_ex - CRi - Cn - mapped_to_a_b_p
#    Cn_ex = Cn - ob_ex - CRi - Ps - mapped_to_a_b_p
#elif 'BTIRed_Bac' in argv[1]:
ob_ex = ob_ex
CRi_ex = CRi - (ob_ex | Ps | Cn | Pd | Hd | Ss | Ph | Al | Pa | Ea) - mapped_to_a_b_p - Ps - Cn - Pd - Hd - Ss - Ph - Al - Pa - Ea
Ps_ex = Ps - (ob_ex | Cn | Pd | Hd | Ss | Ph | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Cn - Pd - Hd - Ss - Ph - Al - Pa - Ea
Cn_ex = Cn - (ob_ex | Ps | Pd | Hd | Ss | Ph | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Pd - Hd - Ss - Ph - Al - Pa - Ea
Pd_ex = Pd - (ob_ex | Ps | Cn | Hd | Ss | Ph | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Hd - Ss - Ph - Al - Pa - Ea
Hd_ex = Hd - (ob_ex | Ps | Cn | Pd | Ss | Ph | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Ss - Ph - Al - Pa - Ea
Ss_ex = Ss - (ob_ex | Ps | Cn | Pd | Hd | Ph | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Hd - Ph - Al - Pa - Ea
Ph_ex = Ph - (ob_ex | Ps | Cn | Pd | Hd | Ss | Al | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Hd - Ss - Al - Pa - Ea
Al_ex = Al - (ob_ex | Ps | Cn | Pd | Hd | Ss | Ph | Pa | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Hd - Ss - Ph - Pa - Ea
Pa_ex = Pa - (ob_ex | Ps | Cn | Pd | Hd | Ss | Ph | Al | Ea | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Hd - Ss - Ph - Al - Ea
Ea_ex = Ea - (ob_ex | Ps | Cn | Pd | Hd | Ss | Ph | Al | Pa | CRi) - mapped_to_a_b_p - CRi - Ps - Cn - Pd - Hd - Ss - Ph - Al - Pa
#else:
#    pass
# Ps_ex = Ps - CRi - ob - aphid - buchnera - plant
# CRi_ex = CRi - Ps - ob - aphid - buchnera - plant

#with open(argv[5], 'w') as f:
#    f.write('Total: {}\n'.format((len(aphid | buchnera | plant | ob)/totalreads)*100))
# print('All: ', len(aphid & buchnera & plant))
# print('Aphid and plant: ', len((aphid & plant) - buchnera))
# print('Aphid and Buchnera: ', len((aphid & buchnera) - plant))
# print('Buchnera and Plant: ', len((buchnera & plant) - aphid))
# print('Aphid: ', len(aphid - buchnera - plant))
# print('Buchnera: ', len(buchnera - aphid - plant))
# print('Plant: ', len(plant - aphid - buchnera))
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

#with open('/nethome/mct30/bmds/org_names.pkl', 'rb') as list_file:
##with open('org_names.pkl', 'rb') as list_file:
#    org_names = pickle.load(list_file)

for org_set in org_names:
    name = org_set[0]
    accession = org_set[1]
    description = org_set[2]
    try:
        description = description[:description.index(',')]
    except ValueError:
        if 'complete' in description:
            description = description[:description.index(' complete')]
        elif 'chromosome' in description:
            description = description[:description.index(' chromosome')]
    try:
        genomes_dict[description] = genomes_dict.pop(accession)
        genomes_dict_collapsed.setdefault(name, []).extend(genomes_dict[description])
    except KeyError:
        pass
        # if nothing has mapped to the genome from org_names, it won't be in 
        # genome_dict

ordered_list = sorted(genomes_dict_collapsed, key=lambda x: (len(genomes_dict_collapsed[x]), x), reverse = True)

with open(argv[5], 'w') as f:
#    f.write('{}\t\t\t\n'.format(argv[1]))
    f.write('{}\t\t\n'.format(argv[1].lstrip('/nethome/mct30/bmds/SAM_out/').rstrip('_Myzus-only.map').replace('_', ' ').replace('Bac', 'Bacteriome')))
    # f.write('Total: {}%\n'.format(round((len(aphid | buchnera | plant | ob)/totalreads)*100, 2)))
    # f.write('All: {}%\n'.format(round((len(aphid & buchnera & plant)/totalreads)*100, 2)))
    # f.write('Aphid and plant: {}%\n'.format(round((len((aphid & plant) - buchnera)/totalreads)*100, 2)))
    # f.write('Aphid and Buchnera: {}%\n'.format(round((len((aphid & buchnera) - plant)/totalreads)*100, 2)))
    # f.write('Buchnera and Plant: {}%\n'.format(round((len((buchnera & plant) - aphid)/totalreads)*100, 2)))
    # f.write('Aphid: {}%\n'.format(round((len(aphid - buchnera - plant)/totalreads)*100, 2)))
    # f.write('Buchnera: {}%\n'.format(round((len(buchnera - aphid - plant)/totalreads)*100, 2)))
    # f.write('Plant: {}%\n'.format(round((len(plant - aphid - buchnera)/totalreads)*100, 2)))
    # f.write('Other Bacteria Exclusively: {0}%\t{1}\n'.format(round((len(ob_ex)/totalreads)*100, 2), len(ob_ex)))
    # try:
    #     f.write('Pseudomonas syringae pv. tomato str. DC3000 Exclusively: {0}%\t{1}\n'.format(round((len(Ps_ex)/totalreads)*100, 2), len(Ps_ex)))
    # except:
    #     pass
    # try:
    #     f.write('Candidatus Regiella insecticola 5.15 Exclusively: {0}%\t{1}\n'.format(round((len(CRi_ex)/totalreads)*100, 2), len(CRi_ex)))
    # except:
    #     pass
    # try:
    #     f.write('Cupriavidus necator N-1 Exclusively: {0}%\t{1}\n'.format(round((len(Cn_ex)/totalreads)*100, 2), len(Cn_ex)))
    # except:
    #     pass
    # try:
    #     f.write('Paenibacillus daejeonensis DSM 15491 Exclusively: {0}%\t{1}\n'.format(round((len(Pd_ex)/totalreads)*100, 2), len(Pd_ex)))
    # except:
    #     pass
    f.write('Total: {0}%\t{1}\n'.format(round((len(aphid | buchnera | plant | ob)/totalreads)*100, 2), len(aphid | buchnera | plant | ob)))
    f.write('All: {0}%\t{1}\n'.format(round((len(aphid & buchnera & plant)/totalreads)*100, 2), len(aphid & buchnera & plant)))
    f.write('Aphid and plant: {0}%\t{1}\n'.format(round((len((aphid & plant) - buchnera)/totalreads)*100, 2), len((aphid & plant) - buchnera)))
    f.write('Aphid and Buchnera: {0}%\t{1}\n'.format(round((len((aphid & buchnera) - plant)/totalreads)*100, 2), len((aphid & buchnera) - plant)))
    f.write('Buchnera and Plant: {0}%\t{1}\n'.format(round((len((buchnera & plant) - aphid)/totalreads)*100, 2), len((buchnera & plant) - aphid)))
    f.write('Aphid: {0}%\t{1}\n'.format(round((len(aphid - buchnera - plant)/totalreads)*100, 2), len(aphid - buchnera - plant)))
    f.write('Buchnera: {0}%\t{1}\n'.format(round((len(buchnera - aphid - plant)/totalreads)*100, 2), len(buchnera - aphid - plant)))
    f.write('Plant: {0}%\t{1}\n'.format(round((len(plant - aphid - buchnera)/totalreads)*100, 2), len(plant - aphid - buchnera)))
    f.write('Other Bacteria Total without Aphid, Buchnera, and Plant: {0}%\t{1}\n'.format(round((len(ob_ex)/totalreads)*100, 2), len(ob_ex)))
    try:
        f.write('Pseudomonas syringae pv. tomato str. DC3000 Exclusively: {0}%\t{1}\n'.format(round((len(Ps_ex)/totalreads)*100, 2), len(Ps_ex)))
    except:
        pass
    try:
        f.write('Candidatus Regiella insecticola 5.15 Exclusively: {0}%\t{1}\n'.format(round((len(CRi_ex)/totalreads)*100, 2), len(CRi_ex)))
    except:
        pass
    try:
        f.write('Cupriavidus necator N-1 Exclusively: {0}%\t{1}\n'.format(round((len(Cn_ex)/totalreads)*100, 2), len(Cn_ex)))
    except:
        pass
    try:
        f.write('Paenibacillus daejeonensis DSM 15491 Exclusively: {0}%\t{1}\n'.format(round((len(Pd_ex)/totalreads)*100, 2), len(Pd_ex)))
    except:
        pass
    try:
        f.write('Candidatus Hamiltonella defensa Exclusively: {0}%\t{1}\n'.format(round((len(Hd_ex)/totalreads)*100, 2), len(Hd_ex)))
    except:
        pass
    try:
        f.write('Serratia symbiotica Exclusively: {0}%\t{1}\n'.format(round((len(Ss_ex)/totalreads)*100, 2), len(Ss_ex)))
    except:
        pass
    try:
        f.write('Paenibacillus herberti Exclusively: {0}%\t{1}\n'.format(round((len(Ph_ex)/totalreads)*100, 2), len(Ph_ex)))
    except:
        pass
    try:
        f.write('Candidatus Arsenophonus lipoptenae Exclusively: {0}%\t{1}\n'.format(round((len(Al_ex)/totalreads)*100, 2), len(Al_ex)))
    except:
        pass
    try:
        f.write('Pseudomonas aeruginosa PAO1 Exclusively: {0}%\t{1}\n'.format(round((len(Pa_ex)/totalreads)*100, 2), len(Pa_ex)))
    except:
        pass
    try:
        f.write('Erwinia aphidicola Exclusively: {0}%\t{1}\n'.format(round((len(Ea_ex)/totalreads)*100, 2), len(Ea_ex)))
    except:
        pass
#    f.write('Percentage\tNumber of Reads\tOrganism Name\n')
    for entry in ordered_list:
        readnums = genomes_dict_collapsed[entry]
        refgen = entry
#        count = len(readnums) - 1
#        # -1 accounts for added description at the end
        count = len(readnums)
        genomes_dict_collapsed[refgen].append(count)
        # Appends a new entry to end of readnums list with
        # the number of matched reads for that genome
        percent = round(((count/totalreads)*100), 4)
        # Calculates the percent of total reads mapped to that ggenome
        genomes_dict_collapsed[refgen].append(percent)
        # genomes_dict[genome] = {read1, read2, ... , count, percentage}
#        f.write('%s%%\t%s\t%s\t%s\n' % (percent, count, refgen, readnums[-3]))
        f.write('{0}\t\t{1}%\t\t\t{2}\n'.format(refgen, percent, count))

