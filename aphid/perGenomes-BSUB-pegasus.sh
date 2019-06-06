#! /bin/bash

#BSUB -J perGenomes_3
#BSUB -e /nethome/mct30/err/perGenomes_3.err
#BSUB -o /nethome/mct30/out/perGenomes_3.out
#BSUB -n 1
#BSUB -P acypi
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

module switch python/3.6.5 > /dev/null 2>&1
# Need to work in python3
# Should silence error output


#
# Percentage for Genomes
#

cd /nethome/mct30/bmds/SAM_out/
for filename in *_other_bacteria_HF_2018.map; do
    python /nethome/mct30/gitclones/bmds/aphid/perGenomes.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done
for filename in *_CRi.map; do
    python /nethome/mct30/gitclones/bmds/aphid/perGenomes.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done
