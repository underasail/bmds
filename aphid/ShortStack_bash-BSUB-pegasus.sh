#! /bin/bash

#BSUB -J ShortStack-bash
#BSUB -e /nethome/mct30/err/ShortStack-bash.err
#BSUB -o /nethome/mct30/out/ShortStack-bash.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -R "rusage[mem=31000]"
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

/nethome/mct30/acypi/sra/plants/ShortStack_miRNA.sh