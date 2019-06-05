
# USAGE = ./fetchGenomes.py [CSV FILE WITH ORGANISMS] [/root/path/to/ref_genomes_folder/] [/path/to/genomes_downloaded.tsv]
# with closing '/' at end of path

#from sys import argv
import csv
from Bio import Entrez
from Bio import SeqIO
from time import sleep

organisms = []
biosample_accession_numbers = []
genebank_ids = []
argv = ['', 'HF-lit-search_and_2018-aphid-gut-paper.txt', 
        'C:\\Users\\Thompson\\Documents\\Genomes\\', 
        'C:\\Users\\Thompson\\Documents\\Genomes\\genomes_included.tsv']

Entrez.email = 'Thompson.Max.C@miami.edu'
with open(argv[1], newline='') as f:
    # next(f)
    # Skips header line
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        organism = row[0]
        organisms.append(organism)

genome_tsv = open(argv[3], 'w')

for organism in organisms:
    sleep(0.5)
    search_term = '"%s"[Organism] AND "reference genome"[RefSeq Category] \
    AND ("full genome representation"[filter]) \
    AND (all[filter] NOT anomalous[filter])' % str(organism)
    # Uses name from lit search as organism; requires hits to be a complete reference genome,
    esearch_handle = Entrez.esearch(db = 'assembly', term = search_term)
    # Use Assembly database to find Assembly DB IDs for complete genomes of organisms
    esearch_result = Entrez.read(esearch_handle)
    esearch_handle.close()
    if esearch_result['Count'] == '0':
        sleep(0.5)
        # Ensure there is at least one genome for the organism
        search_term = '"%s"[Organism] AND "representative genome"[RefSeq Category] \
        AND ("full genome representation"[filter]) \
        AND (all[filter] NOT anomalous[filter])' % str(organism)
        esearch_handle = Entrez.esearch(db = 'assembly', term = search_term)
        esearch_result = Entrez.read(esearch_handle)
        esearch_handle.close()
        if esearch_result['Count'] == '0':
            sleep(0.5)
            search_term = '"%s"[Organism] AND \
            ("full genome representation"[filter]) \
            AND (all[filter] NOT anomalous[filter])' % str(organism)
            esearch_handle = Entrez.esearch(db = 'assembly', term = search_term)
            esearch_result = Entrez.read(esearch_handle)
            esearch_handle.close()
            if esearch_result['Count'] == '0':
                print('%s   N/A Not Included' % str(organism))
                genome_tsv.write("{0}\tN/A\tN/A\tNot Included\n".format(organism))
            elif 'virus' not in str(organism):
                for ID in esearch_result['IdList']:
                    sleep(0.5)
                    esummary_handle = Entrez.esummary(db = 'assembly', id = ID, report = 'full')
                    esummary_result = Entrez.read(esummary_handle)
                    biosample_accession_numbers.append(\
                    esummary_result['DocumentSummarySet']['DocumentSummary'][0]['BioSampleAccn'])
                    refseq_acc = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
                    organism = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Organism']
                    try:
                        sub_type = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_type']
                        sub_value = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']
                        organism = "{0} {1} {2}".format(organism, sub_type, sub_value)
                    except:
                        pass
                    print('%s   Full Genome Included' % str(organism))
                    genome_tsv.write("{0}\tFull Genome\t{1}\tIncluded\n".format(organism, refseq_acc))
            else:
                for ID in esearch_result['IdList']:
                    sleep(0.5)
                    esummary_handle = Entrez.esummary(db = 'assembly', id = ID, report = 'full')
                    esummary_result = Entrez.read(esummary_handle)
                    genebank_ids.append(\
                    esummary_result['DocumentSummarySet']['DocumentSummary'][0]['GbUid'])
                    # GenBank ID Location
                    refseq_acc = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
                    organism = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Organism']
                    try:
                        sub_type = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_type']
                        sub_value = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']
                        organism = "{0} {1} {2}".format(organism, sub_type, sub_value)
                    except:
                        pass
                    print('%s   Full Genome Included' % str(organism))
                    genome_tsv.write("{0}\tFull Genome\t{1}\tIncluded\n".format(organism, refseq_acc))
        else:
            for ID in esearch_result['IdList']:
                sleep(0.5)
                esummary_handle = Entrez.esummary(db = 'assembly', id = ID, report = 'full')
                esummary_result = Entrez.read(esummary_handle)
                biosample_accession_numbers.append(\
                esummary_result['DocumentSummarySet']['DocumentSummary'][0]['BioSampleAccn'])
                refseq_acc = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
                organism = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Organism']
                try:
                    sub_type = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_type']
                    sub_value = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']
                    organism = "{0} {1} {2}".format(organism, sub_type, sub_value)
                except:
                    pass
                print('%s   Representative Genome   Included' % str(organism))
                genome_tsv.write("{0}\tRepresentative Genome\t{1}\tIncluded\n".format(organism, refseq_acc))
    # Nested ifs above serve to search for reference genomes first, then representative
    # if there are no reference, then just complete if there are no representative
    # This limits number of results and insures better quality genomes if available
    else:
        for ID in esearch_result['IdList']:
            sleep(0.5)
            esummary_handle = Entrez.esummary(db = 'assembly', id = ID, report = 'full')
            # Utilize esummary to fetch BioProject Accession number from Assembly IDs
            # https://www.biostars.org/p/141581/
            esummary_result = Entrez.read(esummary_handle)
            biosample_accession_numbers.append(\
            esummary_result['DocumentSummarySet']['DocumentSummary'][0]['BioSampleAccn'])
            # Location of BioProject Assembly Number in resulting dictionary structure
            # BioProject Id allows access to all genomes associated with that Assembly ID, and
            # only those genomes when searching below (RefSeq brought up all for organism)
            # esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
                # Location of RefSeq Accession Number
            # esummary_result['DocumentSummarySet']['DocumentSummary'][0]\
            # ['GB_BioProjects'][0]['BioprojectId'])
                # Location of BioProject ID
            # esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Organism']
                # Location of organism name
            refseq_acc = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession']
            organism = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Organism']
            try:
                sub_type = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_type']
                sub_value = esummary_result['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']
                organism = "{0} {1} {2}".format(organism, sub_type, sub_value)
            except:
                pass
            print('%s   Reference Genome    Included' % str(organism))
            genome_tsv.write("{0}\tReference Genome\t{1}\tIncluded\n".format(organism, refseq_acc))
if len(biosample_accession_numbers) > 0:
    for biosample_accession_number in biosample_accession_numbers:
        sleep(0.5)
        esearch_handle = Entrez.esearch(db = 'nuccore', \
        term = '%s[BioSample] AND biomol_genomic[PROP] \
        NOT "sequencing project"' % biosample_accession_number)
        # Searching BioSample Accession number to get GeneBank IDs for FASTA download
        # Sorted by decreasing sequence length
        # NOT is to avoid WGS projects
        esearch_result = Entrez.read(esearch_handle)
        esearch_handle.close()
        genebank_ids.append(esearch_result['IdList'][0])
        # Only takes the longest complete genome sequence
else:
    pass
    # Viruses should be only thing to pass, and they already have GBIDs

genome_tsv.close()

genebank_ids = list(set(genebank_ids))
#%%
genebank_ids_string = ','.join(genebank_ids)
sleep(0.5)
efetch_handle = Entrez.efetch(db = 'nuccore', id = genebank_ids_string,
                              rettype = 'gb', retmode = 'text')
efetch_records = SeqIO.parse(efetch_handle, 'gb')
filenames = []
for record in efetch_records:
    organism_name = \
    record.annotations['organism'].replace(' ', '_').replace('.', '')
    refseq_acc = record.annotations['accessions'][0]
    filenames.append('_'.join([refseq_acc, organism_name]))
#%%
for filename, genebank_id in zip(filenames, genebank_ids):
    sleep(0.5)
    efetch_handle = Entrez.efetch(db = 'nuccore', id = genebank_id,
                                  rettype = 'fasta', retmode = 'text')
    # Fetches FASTA file for genome
    # filename = '%sGBID%s.fasta' % (argv[2], genebank_id)
    # ex: /root/path/to/ref_genomes_folder/GBID1234567.fasta
    filename = "{0}{1}.fasta".format(argv[2], filename)
    with open(filename, 'w') as f:
        f.write(efetch_handle.read())
        # Writes FASTA file under specified directory
