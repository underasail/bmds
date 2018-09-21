#! /bin/bash

#BSUB -J RNA-parallel
#BSUB -e /nethome/mct30/err/RNA-parallel.err
#BSUB -o /nethome/mct30/out/RNA-parallel.out
#BSUB -P acypi
#BSUB -n 2
#BSUB -q general
#BSUB -W 48:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

# RNAcalibrate -m 10000 -t ~/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta -q ~/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa

parallel --link --eta \
"RNAcalibrate -m 10000 -t {2} -q {1} > {3}" \
::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1.fa \
::: /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_RNAcalibrate.out \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1_RNAcalibrate.out