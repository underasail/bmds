#! /bin/bash

#BSUB -J RNAhybrid
#BSUB -e /nethome/mct30/err/RNAhybrid.err
#BSUB -o /nethome/mct30/out/RNAhybrid.out
#BSUB -n 1
#BSUB -P acypi
#BSUB -q general
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

# RNAhybrid -d 1.838047,0.146773 -e 0 -p 0.05 -f 2,8 -m 10000 \
# -t /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
# AGCGGAAUAUAAGAACUCGUCUCU

/nethome/mct30/gitclones/bmds/aphid/RNAhybrid_call.py \
/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique.fa.annotations \
/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/RNAcalibrate.out