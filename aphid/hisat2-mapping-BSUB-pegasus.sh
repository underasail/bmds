#! /bin/bash

#BSUB -J hisat2-mapping
#BSUB -e /nethome/mct30/err/hisat2-mapping.err
#BSUB -o /nethome/mct30/out/hisat2-mapping.out
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

hisat2 -x /nethome/mct30/bmds/index/LSR1-A_pisum/LSR1-A_pisum \
-p 8 \
-U /projects/scratch/acypi/sra/SRR7037537_trimmed.fq \
| samtools view -bS - > A_pisum_Gut1_LSR1_rnaseq_2.hisat.bam