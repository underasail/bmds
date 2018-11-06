#! /bin/bash

blastn -query ~/temp/fasta.fa -db /nethome/mct30/blastdbs/miRBase_mature -task blastn -word_size 4 -dust no -soft_masking false -num_alignments 2 -num_descriptions 2 -out ~/temp/fasta.out