#! /bin/bash

#BSUB -J afterqc
#BSUB -e /nethome/mct30/err/afterqc.err
#BSUB -o /nethome/mct30/out/afterqc.out
#BSUB -n 1
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

module swtich python/2.7.3

cd /nethome/mct30/acypi/sra/plants/

python /nethome/mct30/local/afterqc/AfterQC-master/after.py --gzip \
--read1_flag SRR7993 -1 SRR799356-58_vdb.fastq