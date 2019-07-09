from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'Thompson.Max.C@miami.edu'

genebank_ids = []

with open('GBIDs.txt', newline='') as f:
    for line in f.readlines():
        genebank_ids.append(line.rstrip('\n'))
genebank_ids_list = ','.join(genebank_ids)
#%%
#for genebank_id in genebank_ids:
efetch_handle = Entrez.efetch(db = 'nuccore', id = genebank_ids_list[10], 
                              rettype = 'gb', retmode = 'text')
#efetch_out = efetch_handle.read()
#print(efetch_out)
efetch_records = SeqIO.parse(efetch_handle, 'gb')
for record in efetch_records:
    organism_name = record.annotations['organism']
    refseq_acc = record.annotations['accessions'][0]
    print(organism_name, refseq_acc)