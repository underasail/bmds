#! /bin/bash

#BSUB -J miR-PREFeR_SRA
#BSUB -e /nethome/mct30/err/miR-PREFeR_SRA.err
#BSUB -o /nethome/mct30/out/miR-PREFeR_SRA.out
#BSUB -P acypi
#BSUB -n 8
#BSUB -q bigmem
#BSUB -R "span[ptile=16]"
#BSUB -R "rusage[mem=31200]"
#BSUB -W 115:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module switch python/2.7.3

/nethome/mct30/local/miR-PREFeR/miR-PREFeR/miR_PREFeR.py \
-L -k \
pipeline \
/nethome/mct30/acypi/sra/plants/miR-PREFeR_SRA_ca27.config
# /nethome/mct30/local/miR-PREFeR/miR-PREFeR/miR-PREFeR.config
# /nethome/mct30/local/miR-PREFeR/miR-PREFeR/miR-PREFeR_SRA.config
