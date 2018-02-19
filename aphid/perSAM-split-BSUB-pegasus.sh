#! /bin/bash

#BSUB -J perSAM-split
#BSUB -e /nethome/mct30/err/perSAM-split.err
#BSUB -o /nethome/mct30/out/perSAM-split.out
#BSUB -n 4
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

module switch python/3.3.1 > /dev/null 2>&1
# need to work in python3

cd /nethome/mct30/bmds/SAM_out/
for filename in *-only.map; do
    /nethome/mct30/gitclones/bmds/aphid/perSAM.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done
# Gets percentage of matched reads for Buchnera and Myzus genomes split
