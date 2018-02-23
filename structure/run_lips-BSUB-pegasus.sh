#! /bin/bash

#BSUB -J run_lips
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

/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle\
/main/source/src/apps/public/membrane_abinitio/run_lips.pl \
/nethome/mct30/aphid/acypi8971_prot.fa \
/nethome/mct30/aphid/acypi8971_octopus.span \
/nethome/mct30/legacy_blast/blast-2.2.26/bin/blastpgp \
/nethome/mct30/nrdb/nr \
/nethome/mct30/rosetta/rosetta_bin_linux_2017.08.59291_bundle\
/main/source/src/apps/public/membrane_abinitio/alignblast.pl
