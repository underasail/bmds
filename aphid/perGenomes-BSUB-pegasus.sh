#! /bin/bash

#BSUB -J perGenomes
#BSUB -e /nethome/mct30/perGenomes.err
#BSUB -o /nethome/mct30/perGenomes.out
#BSUB -n 4
#BSUB -R "rusage[mem=6500]"
#BSUB -q general
#BSUB -W 72:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores, RAM per core in MB,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module switch python/3.3.1 > /dev/null 2>&1
# Need to work in python3
# Should silence error output


#
# Percentage for Genomes
#

cd /nethome/mct30/bmds/SAM_out/
for filename in *.map; do
    /nethome/mct30/gitclones/bmds/aphid/perGenomes.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done

