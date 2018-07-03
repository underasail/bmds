#! /bin/bash

#BSUB -J miranda-parallel
#BSUB -e /nethome/mct30/err/miranda-parallel.err
#BSUB -o /nethome/mct30/out/miranda-parallel.out
#BSUB -P acypi
#BSUB -n 2
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

parallel --link --eta \
"miranda {1} {2} -sc 80 -go -8 -ge -2 -scale 2 -en 0 -strict -quiet -out {3}" \
::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/2_run_15_04_2018_t_09_35_24/result_2.fa \
::: /nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_three_prime_utr_shuffled.fasta \
::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_miranda_three_prime_utr_targets_shuffled.out \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/2_run_15_04_2018_t_09_35_24/result_2_miranda_three_prime_utr_targets_shuffled.out
