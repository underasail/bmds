#! /bin/bash

#BSUB -J tapir_hybrid
#BSUB -e /nethome/mct30/err/tapir_hybrid.err
#BSUB -o /nethome/mct30/out/tapir_hyrbid.out
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

tapir_hybrid \
/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique.fa.annotations \
/nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/target_prediction/plant/psRNATarget/oleracea_transcripts.fa \
| hybrid_parser > /nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/target_prediction/plant/tapir/defaults.txt