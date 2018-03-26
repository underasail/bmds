#! /bin/bash

#BSUB -J miRDeep2
#BSUB -e /nethome/mct30/err/miRDeep2.err
#BSUB -o /nethome/mct30/out/miRDeep2.out
#BSUB -n 1
#BSUB -q general
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

cd /nethome/mct30/bmds/miRDeep2/

/nethome/mct30/gitclones/mirdeep2/bin/miRDeep2.pl \
/nethome/mct30/bmds/G006_Gut_F_trimmed_17-35_seqx_collapsed.fa \
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_noheader.fasta \
/nethome/mct30/bmds/G006_Gut_mapped_seqreadid2.arf none /nethome/mct30/bmds/api_miRNAs.fa none
# Path to program
# Input FASTA reads file
# Input genome FASTA with no whitespaces in header
# Input ARF file with 'seq_x' before each read number 
#     sed "s/^/seq_x/" ~/bmds/G006_Gut_mapped.arf > 
#     ~/bmds/G006_Gut_mapped_seqreadid.arf
# Input file of miRNAs from A pisum