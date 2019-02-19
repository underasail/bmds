#! /bin/bash

#BSUB -J sra_vdb
#BSUB -e /nethome/mct30/err/sra_vdb.err
#BSUB -o /nethome/mct30/out/sra_vdb.out
#BSUB -n 3
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

cd /projects/scratch/acypi/sra/plants
parallel \
"vdb-dump {} -f fastq --output-file ./{}_vdb.fastq" \
::: SRR799356 SRR799357 SRR799358
# ::: SRR6517746 SRR6517744 SRR6517743 SRR6517740 SRR6517739 SRR6517738 SRR6517737
# ::: SRR3239551 SRR3239558 SRR3239552 SRR3239550 SRR7037540 SRR7037537
# vdb-dump SRR6517746 -f fastq --output-file /nethome/mct30/acypi/sra/plants/SRR6517746_vdb.fastq