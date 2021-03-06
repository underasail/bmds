#! /bin/bash

#BSUB -J sra-fastqc
#BSUB -e /nethome/mct30/err/sra-fastqc.err
#BSUB -o /nethome/mct30/out/sra-fastqc.out
#BSUB -n 8
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
# sra-fastqc[37-40,42-46]

module load fastqc java/1.8.0_60

export _JAVA_OPTIONS=-Xmx1500m

cd /nethome/mct30/acypi/sra/plants/fastqc

/nethome/mct30/local/fastqc/FastQC/fastqc \
-o ./ -j /share/opt/java/jdk1.8.0_60/bin/java --noextract -t 8 \
../SRR799356-58_vdb.fastq

# ../SRR65177$LSB_JOBINDEX\_vdb.fastq