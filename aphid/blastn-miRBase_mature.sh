#! /bin/bash

# blastn -query ~/temp/fastqcfa.fa -db /nethome/mct30/blastdbs/miRBase_mature -task blastn -word_size 4 -dust no -soft_masking false -evalue 0.001 -num_alignments 2 -num_descriptions 2 -out ~/temp/fastqcfa.out

# evalue <= 0.001

blastn -query ~/temp/fastqcfa.fa -db /nethome/mct30/blastdbs/ShortStack_0.25rpmm_20-24_f_300_SRA-ca27_MIRNAs -task blastn -word_size 4 -dust no -soft_masking false -evalue 0.001 -num_alignments 2 -num_descriptions 2 -out ~/temp/fastqcfa.out