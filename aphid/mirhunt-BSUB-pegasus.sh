#! /bin/bash

#BSUB -J mirhunt-parallel
#BSUB -e /nethome/mct30/err/mirhunt-parallel.err
#BSUB -o /nethome/mct30/out/mirhunt-parallel.out
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

# mirhunt multi target=/nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta query=/nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa output=/nethome/mct30/bmds/plant/predictions/

parallel --link --eta \
"mirhunt multi target={2} query={1} output={3}" \
::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fas \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1.fas \
::: /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fas \
::: /nethome/mct30/bmds/plant/predictions/mirhunt \
/nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/mirhunt