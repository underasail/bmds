#! /share/opt/python/3.3.1/bin/python

# USAGE = ./fetchGenomes.py [CSV FILE WITH ORGANISMS] [/root/path/to/ref_genomes_folder/]
# with closing '/' at end of path

from sys import argv
import csv
from Bio import Entrez

organisms = []
accession_numbers = []
genebank_ids = []

Entrez.email = 'mct30@miami.edu'

with open(argv[1], newline='') as f:
    next(f)
    # Skips header line
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        organism = row[0]
        organisms.append(organism)

for organism in organisms:
    search_term = '"%s"[Organism] AND ("reference genome"[RefSeq Category] \
    OR "representative genome"[RefSeq Category] OR "complete genome"[Assembly Level]) \
    AND ("latest refseq"[filter] AND all[filter] NOT anomalous[filter])' % str(organism)
    # Uses name from lit search as organism; requires hits to be a reference genome,
    # representative genome, or a complete genome. Hits are then filtered.
    esearch_handle = Entrez.esearch(db = 'assembly', term = search_term)
    # Use Assembly database to find Assembly DB IDs for complete genomes of organisms
    esearch_result = Entrez.read(esearch_handle)
    esearch_handle.close()
    if esearch_result['Count'] == '0':
        print('No hits for %s' % str(organism))
        # Ensure there is at least one genome for the organism
    else:
        for ID in esearch_result['IdList']:
            esummary_handle = Entrez.esummary(db = 'assembly', id = ID, report = 'full')
            # Utilize esummary to fetch BioProject Accession number from Assembly IDs
            # https://www.biostars.org/p/141581/
            esummary_result = Entrez.read(esummary_handle)
            accession_numbers.append(\
            esummary_result['DocumentSummarySet']['DocumentSummary'][0]\
            ['GB_BioProjects'][0]['BioprojectId'])
            # Location of BioProject Assembly Number in resulting dictionary structure
            # BioProject Id allows access to all genomes associated with that Assembly ID, and
            # only those genomes when searching below (RefSeq brought up all for organism)
            # esummary_result['DocumentSummarySet']['DocumentSummary'][0]['AssemblyAccession'])
                # Location of RefSeq Accession Number
for accession_number in accession_numbers:
    esearch_handle = Entrez.esearch(db = 'nuccore', \
    term = '%s[BioProject]' % accession_number)
    # Searching BioProject Accession number to get GeneBank IDs for FASTA download
    esearch_result = Entrez.read(esearch_handle)
    esearch_handle.close()
    genebank_ids.extend(esearch_result['IdList'])
    # If there are multiple results, should add them all indivudally
for genebank_id in genebank_ids:
    efetch_handle = Entrez.efetch(db = 'nuccore', id = genebank_id, rettype = 'fasta', retmode = 'text')
    # Fetches FASTA file for genome
    filename = '%sGBID%s.fasta' % (argv[2], genebank_id)
    # ex: /root/path/to/ref_genomes_folder/GBID1234567.fasta
    with open(filename, 'w') as f:
        f.write(efetch_handle.read())
        # Writes FASTA file under specified directory 
    print('GeneBank ID: %s saved under %s' % (genebank_id, filename))
