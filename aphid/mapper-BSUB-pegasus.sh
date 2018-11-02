#! /bin/bash

#BSUB -J mapper
#BSUB -e /nethome/mct30/err/mapper.err
#BSUB -o /nethome/mct30/out/mapper.out
#BSUB -n 1
#BSUB -P acypi
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

cd /nethome/mct30/gitclones/mirdeep2/

/nethome/mct30/gitclones/mirdeep2/bin/mapper.pl \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plant-Myzus-only.fasta -c \
-p /nethome/mct30/bmds/index/bt1-G006-Myzus/bt1-G006-Myzus-index \
-t /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plant-Myzus-only_mapped.arf
# Input FASTA file (-c) of reads
# -p 'path to genome index'
# -q with one mismatch
# -t output mapped arf file