#! /bin/bash

#BSUB -J ShortStack-bash-single
#BSUB -e /nethome/mct30/err/ShortStack-bash-single.err
#BSUB -o /nethome/mct30/out/ShortStack-bash-single.out
#BSUB -n 8
#BSUB -P mtor
#BSUB -q bigmem
#BSUB -W 115:00
#BSUB -R "rusage[mem=5000]"
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB (-R "rusage[mem=31000]" -R "span[ptile=16]")

# /nethome/mct30/acypi/sra/plants/ShortStack_miRNA_single_$LSB_JOBINDEX.sh
/nethome/mct30/acypi/sra/plants/ShortStack_miRNA_single_2.sh