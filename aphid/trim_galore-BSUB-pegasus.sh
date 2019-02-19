#! /bin/bash

#BSUB -J trim-galore
#BSUB -e /nethome/mct30/err/trim-galore.err
#BSUB -o /nethome/mct30/out/trim-galore.out
#BSUB -n 6
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

module load fastqc/0.10.1

cd /projects/scratch/acypi/sra
parallel \
"trim_galore --fastqc {}.fastq" \
::: SRR3239551 SRR3239558 SRR3239552 SRR3239550 SRR7037540 SRR7037537