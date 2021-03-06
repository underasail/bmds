#! /bin/bash

#BSUB -J ob-align
#BSUB -e /nethome/mct30/err/ob-align.err
#BSUB -o /nethome/mct30/out/ob-align.out
#BSUB -n 8
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

module load bowtie2

bowtie2 -L 10 -f -p 8 --no-unal --very-sensitive -a --no-hd \
-x /nethome/mct30/bmds/index/other_bacteria/other_bacteria_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_other_bacteria_sensitive_all.map
# G006 gut reads aligned against the other_bacteria