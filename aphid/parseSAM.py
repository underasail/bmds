#! /share/opt/python/3.3.1/bin/python

# Usage: ./parseSAM.py [INPUT SAM FILE] ['percent OR 'parsed' (see choice below) (> Results passed to stdout, redirect with carrot to generate output file)

from sys import argv
import csv
from Bio import Entrez
from Bio import SeqIO

choice = argv[2]
# choice = input('Output genome percentage rankings [percent] or parsed genename, genome, sequence data [parsed]: ')
# make decsion on output format,
#   percent will output a listing for each genome 
#       with name, description, and number of and percentage of reads matched
#   parsed will output an entry for each matched read 
#       with the read name, aligned genome, and sequence in a \t deliminated format
if choice == 'percent':
    pass
elif choice == 'parsed':
    pass
else:
    sys.exit('ChoiceError: Please choose only "percent" or "parsed"')

totalreads = 0
refdict = {}
gi_list = list()

if choice == 'parsed':
    refdict_seq = {}
    sorted_list = []
else: # choice == 'percent'
    refdict_count = {}
    refdict_per = {}
    all_list = list()
    refdict_alltogether = {}

"""Parsing of Bowtie2 SAM Output"""
with open(argv[1], newline='') as f:
    next(f)
    next(f)
    next(f)
    csvreader = csv.reader(f, delimiter = '\t')
    for row in csvreader:
        if len(row) >= 14:
            if 'XM:i:0' or 'XM:i:1' or 'XM:i:2' in str(row):
                # use to select only for allignments with two or fewer mismatchesashr
                readnum = row[0]
                refgen = row[2]
                seq = row[9]
                # http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#sam-output
                # Set up ref genome as key and append read numbers as values
                refdict.setdefault(refgen, []).append(readnum)
                # allows entry to be created if not and added to without disruption if previously generated
                refdict_seq.setdefault(refgen, []).append(seq)
        else:
            pass

if 'G002' in argv[1]:
    totalreads = 12085742
elif 'G006' in argv[1]:
    totalreads = 21960873
elif 'BTIRed' in argv[1]:
    totalreads = 13931847


"""Determination of Number of Sequences per Reference Genome"""
if choice == 'percent':
    for key, value in refdict.items():
        refdict_count.setdefault(key, []).append(len(value))
        # estabilishes dictionary with GIs as keys and number of sequences mapped to that ref genome as value
    for key, value in refdict_count.items():
        percent = round(((value[0]/totalreads)*100), 2)
        refdict_per.setdefault(key, []).append(percent)
        # Sums total reads caught and generates a percent for each reference genome
else: # choice == 'parsed'
    pass


"""Use NCBI to Generate SeqRecord Object for Reference Genomes"""
# Need to generate a list of the keys(Genebank Identifiers)
# List will be searched against NCBI using Entrez
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc131
GIs = list(refdict.keys())
Entrez.email = 'mct30@miami.edu'
for (entry, olddictkey) in zip(GIs, refdict.keys()):
    handle = Entrez.esearch(db='nuccore', term = entry)
    record = Entrez.read(handle)
    result = record['IdList']
    # print(type(result)) returns: <class 'Bio.Entrez.Parser.ListElement'>
    # result = result[0] returned index error saying list index out of range on full dataset
    # gi_list.append(result) to avoid above problem, used below instead
    gi_list = gi_list + result
    refdict[gi_list[-1]] = refdict.pop(olddictkey)
    # changes keys in primary dictionary to GeneBank Identifiers unstead of SAM ID
gi_str = ",".join(gi_list)

handle = Entrez.efetch(db='nuccore', id=gi_str, rettype='gb', retmode='text') 
# Biopython should convert the query to a string of query GIs separated by commas (123,234,345)
# Genome database no longer supported for efretch calls; nuccore contains better info
# https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec:entrez-search-fetch-genbank
records = SeqIO.parse(handle, 'gb')

if choice == 'percent':
    for (record, GI, count, per, seq) in zip(records, gi_list, refdict_count.values(), refdict_per.values(), readdict_seq.values()):
        # record is a SeqRecord object and has all of its attributes
        # http://biopython.org/DIST/docs/api/Bio.SeqRecord-pysrc.html#SeqRecord.__init__
        all_list.append(GI)
        all_list.append(record.description)
        all_list.append(count[0])
        all_list.append(per[0])
        refdict_alltogether.setdefault(record.id, []).append(all_list)
        # builds a final dictionary that houses all pertinate attributes stored under the SeqRecord ID/sequence ID
        print('"""%s"""\nGenBank Identifier: %s\nDescription: %s\nNumber of matched reads: %s\nTotal reads mapped to this genome: %s%%\n' % (record.id, GI, record.description, count[0], per[0]))
else: # choice == 'parsed'
    pass


"""Output CSV"""
sorteddict = {}

if choice == 'parsed':
    for ((GI, readnums), (key, seqs)) in zip(refdict.items(), refdict_seq.items()):
        # iterates over the values while carrying the keys for the two dictionaries simultaneously
        values = []
        values.extend(readnums)
        seqlist = []
        seqlist.extend(seqs)
        for (genename, seq) in zip(values, seqlist):
            thing = []
            thing.append(genename)
            thing.append(GI)
            thing.append(seq)
            sorted_list.append(thing)
            # print('%s\t%s\t%s' % (genename, GI, seq))
            # sends the parsed results to stdout
    print(sorted_list[-1][0])
    for i in sorted_list:
        print('%s\t%s\t%s' % (i[0], i[1], i[2]))
else: # choice == 'percent'
    pass
