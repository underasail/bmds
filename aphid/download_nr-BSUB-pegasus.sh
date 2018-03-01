#! /bin/bash

#BSUB -J download_nr
#BSUB -e /nethome/mct30/err/download_nr.err
#BSUB -o /nethome/mct30/out/download_nr.out
#BSUB -n 1
#BSUB -q general
#BSUB -W 72:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

cd /nethome/mct30/nrdb/
/nethome/mct30/blast+/ncbi-blast-2.7.1+/bin/update_blastdb.pl nr

for filename in nr*.tar.gz; do
    tar -xzf $filename
done
