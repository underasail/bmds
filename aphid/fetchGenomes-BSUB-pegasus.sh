#! /bin/bash

#BSUB -J fetchGenomes
#BSUB -e /nethome/mct30/fetchGenomes.err
#BSUB -o /nethome/mct30/fetchGenomes.out
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

module switch python/3.3.1
# need to work in python3


#
# Plants
#

/nethome/mct30/gitclones/bmds/aphid/fetchGenomes.py \
/nethome/mct30/bmds/associated/aphid-associated-plant.csv \
/nethome/mct30/bmds/ref_genomes/plants/
# Uses BioPython to fetch genomes of aphid associated plants
# and download them in FASTA format


#
# Other Bacteria
#

/nethome/mct30/gitclones/bmds/aphid/fetchGenomes.py \
/nethome/mct30/bmds/associated/aphid-associated-other_bacteria.csv \
/nethome/mct30/bmds/ref_genomes/other_bacteria/
# Uses BioPython to fetch genomes of aphid associated other bacteria
# and download them in FASTA format


#
# Viruses
#

/nethome/mct30/gitclones/bmds/aphid/fetchGenomes.py \
/nethome/mct30/bmds/associated/aphid-associated-viruses.csv \
/nethome/mct30/bmds/ref_genomes/viruses/
# Uses BioPython to fetch genomes of aphid associated viruses
# and download them in FASTA format

#
# Directory Structure
#

# /nethome/mct30/bmds/
# ├ associated
# │   ├ aphid-associated-other_bacteria.csv
# │   ├ aphid-associated-plant.csv
# │   └ aphid-associated-viruses.csv
# ├ ref_genomes
# │   ├ other_bacteria
# │   ├ plants
# │   └ viruses