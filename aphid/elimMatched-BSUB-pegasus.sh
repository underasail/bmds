#! /bin/bash

#BSUB -J eliminate_matched
#BSUB -e /nethome/mct30/eliminate_matched.err
#BSUB -o /nethome/mct30/eliminate_matched.out
#BSUB -n 1
#BSUB -R "rusage[mem=6500]"
#BSUB -q general
#BSUB -W 72:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores, RAM per core in MB,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module switch python/3.3.1
# need to work in python3


#
# G002
#

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G002_Bac_Buchnera.map \
/nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G002 bacteriocyte reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G002_Gut_Buchnera.map \
/nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G002 gut reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus


#
# G006
#

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G006_Bac_Buchnera.map \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G006 bacteriocyte reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G006_Gut_Buchnera.map \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G006 gut reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus


#
# BTIRed
#

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/BTIRed_Bac_Buchnera.map \
/nethome/mct30/bmds/reads/BTIRed_Bac_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/BTIRed_Bac_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for BTIRed bacteriocyte reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/BTIRed_Gut_Buchnera.map \
/nethome/mct30/bmds/reads/BTIRed_Gut_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/BTIRed_Gut_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for BTIRed gut reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus
