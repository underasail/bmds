#! /bin/bash

#BSUB -J cutadapt
#BSUB -e /nethome/mct30/err/cutadapt.err
#BSUB -o /nethome/mct30/out/cutadapt.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module load python/3.6.5

cd ~/acypi/sra/plants

cutadapt -q 28 --cores=8 -o ./SRR6517737-46_vdb_q28.fasta ./SRR6517737-46_vdb.fastq
#--maximum-length=29 --cores=8 -o ./SRR6517737-46_vdb_ca27.fasta ./SRR6517737-46_vdb.fastq