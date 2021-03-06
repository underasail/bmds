#! /bin/bash

#BSUB -J eliminate_unmatched_G002
#BSUB -e /nethome/mct30/err/eliminate_unmatched_G002.err
#BSUB -o /nethome/mct30/out/eliminate_unmatched_G002.out
#BSUB -n 6
#BSUB -P acypi
#BSUB -R "span[ptile=16]"
#BSUB -R "rusage[mem=1500]"
#BSUB -q general
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores, RAM per core in MB,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module switch python/3.6.5 > /dev/null 2>&1
# need to work in python3


##############################################
# G006 Buchnera, Myzus, and plant only FASTA #
##############################################

parallel --link -j 6 \
'/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/{1} \
/nethome/mct30/bmds/reads/{2} \
/nethome/mct30/bmds/reads/{3}' \
::: G002_Bac_Myzus-only.map G002_Gut_Myzus-only.map \
G002_Bac_Buchnera-only.map G002_Gut_Buchnera-only.map \
G002_Bac_plants-only.map G002_Gut_plants-only.map \
::: G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
::: G002_Bac_trimmed_17-35_Myzus.fasta G002_Gut_trimmed_17-35_Myzus.fasta \
G002_Bac_trimmed_17-35_Buchnera.fasta G002_Gut_trimmed_17-35_Buchnera.fasta \
G002_Bac_trimmed_17-35_plants.fasta G002_Gut_trimmed_17-35_plants.fasta
