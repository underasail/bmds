#! /bin/bash

#BSUB -J eliminate_unmatched
#BSUB -e /nethome/mct30/eliminate_unmatched.err
#BSUB -o /nethome/mct30/eliminate_unmatched.out
#BSUB -n 1
#BSUB -R "rusage[mem=7000]"
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

module switch python/3.6.5
# need to work in python3


##############
# G006 Myzus #
##############

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Bac_Myzus-only.map \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_Myzus.fasta

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Gut_Myzus-only.map \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_Myzus.fasta

# Filters read files generating new ones that contain
# only reads that mapped to Myzus

#################
# G006 Buchnera #
#################

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Bac_Buchnera-only.map \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_Buchnera.fasta

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Gut_Buchnera-only.map \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_Buchnera.fasta

# Filters read files generating new ones that contain
# only reads that mapped to Buchnera

##############
# G006 Plant #
##############

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Bac_plants-only.map \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_plants.fasta

/nethome/mct30/gitclones/bmds/aphid/elimUnmatched.py \
/nethome/mct30/bmds/SAM_out/G006_Gut_plants-only.map \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta

# Filters read files generating new ones that contain
# only reads that mapped to plant
