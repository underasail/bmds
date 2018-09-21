#! /bin/bash

#BSUB -J miranda-parallel
#BSUB -e /nethome/mct30/err/miranda-parallel_3.err
#BSUB -o /nethome/mct30/out/miranda-parallel_3.out
#BSUB -P acypi
#BSUB -n 1
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

# parallel --link --eta \
# "miranda {1} {2} -sc 0 -go -8 -ge -2 -scale 2 -en 0 -strict -quiet -out {3}" \
# ::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_shuffled.fa \
# /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1_shuffled.fa \
# ::: /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
# ::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_miranda_targets_0_shuffled.out \
# /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1_miranda_targets_0_shuffled.out

miranda /nethome/mct30/bmds/miRDeep2/mirdeep_runs/3_run_23_08_2018_t_20_16_13/animal_miRNAs.fa \
/nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta  \
-sc 80 -go -8 -ge -2 -scale 2 -en 0 -strict -quiet \
-out /nethome/mct30/bmds/miRDeep2/mirdeep_runs/3_run_23_08_2018_t_20_16_13/animal_miRNAs_miranda_targets.out
