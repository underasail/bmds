#! /bin/bash

#BSUB -J perSAM
#BSUB -e /nethome/mct30/perSAM.err
#BSUB -o /nethome/mct30/perSAM.out
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

module switch python/3.3.1
# need to work in python3


#
# Percentage Calculations
#

for filename in /nethome/mct30/bmds/SAM_out/*.map; do
    /nethome/mct30/gitclones/bmds/aphid/perSAM.py \
    $filename;
done