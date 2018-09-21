#! /bin/bash

#BSUB -J miR-PREFeR
#BSUB -e /nethome/mct30/err/miR-PREFeR.err
#BSUB -o /nethome/mct30/out/miR-PREFeR.out
#BSUB -P acypi
#BSUB -n 4
#BSUB -q bigmem
#BSUB -R "span[ptile=16]"
#BSUB -R "rusage[mem=10000]"
#BSUB -W 115:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module load python/2.7.3

/nethome/mct30/local/miR-PREFeR/miR-PREFeR/miR_PREFeR.py \
-L -k \
pipeline \
/nethome/mct30/local/miR-PREFeR/miR-PREFeR/miR-PREFeR.config