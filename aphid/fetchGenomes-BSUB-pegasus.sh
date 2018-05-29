#! /bin/bash

#BSUB -J fetchGenomes
#BSUB -e /nethome/mct30/err/fetchGenomes_2.err
#BSUB -o /nethome/mct30/out/fetchGenomes_2.out
#BSUB -P acypi
#BSUB -n 1
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
# need to work in python3


##################
# Other Bacteria #
##################

/nethome/mct30/gitclones/bmds/aphid/fetchGenomes.py \
/nethome/mct30/bmds/associated/aphid-associated-other_bacteria.csv \
/nethome/mct30/bmds/ref_genomes/other_bacteria/
# Uses BioPython to fetch genomes of aphid associated other bacteria
# and download them in FASTA format


###########
# Viruses #
###########

/nethome/mct30/gitclones/bmds/aphid/fetchGenomes.py \
/nethome/mct30/bmds/associated/aphid-associated-viruses.csv \
/nethome/mct30/bmds/ref_genomes/viruses/
# Uses BioPython to fetch genomes of aphid associated viruses
# and download them in FASTA format


#######################
# Directory Structure #
#######################

# /nethome/mct30/bmds/
# ├ associated
# │   ├ aphid-associated-other_bacteria.csv
# │   ├ aphid-associated-plant.csv
# │   └ aphid-associated-viruses.csv
# ├ ref_genomes
# │   ├ other_bacteria
# │   ├ plants
# │   └ viruses