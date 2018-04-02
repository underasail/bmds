#! /bin/bash

#BSUB -J blastpgp_8971
#BSUB -e /nethome/mct30/err/%J.err
#BSUB -o /nethome/mct30/out/%J.out
#BSUB -n 2
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

/nethome/mct30/legacy_blast/blast-2.2.26/bin/blastpgp\
 -i /nethome/mct30/aphid/8971.fasta \
-d /nethome/mct30/nrdb/nr \
-j 2 -h 0.001 -b5000 -v5000 \
-o /nethome/mct30/aphid/8971.blast