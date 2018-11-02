#! /bin/bash

#BSUB -J pita-parallel
#BSUB -e /nethome/mct30/err/pita-parallel_miR-PREFeR.err
#BSUB -o /nethome/mct30/out/pita-parallel_miR-PREFeR.out
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

# pita_prediction.pl -utr /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta -mir /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa -gxp -gu 0 -prefix /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_pita_targets

# parallel --link --eta \
# "pita_prediction.pl -utr {2} -mir {1} -gxp -gu 0 -prefix {3}" \
# ::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction.fa \
# /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1.fa \
# ::: /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
# ::: /nethome/mct30/bmds/plant/predictions/G006_Gut_plant_filter_P_prediction_pita_targets_ \
# /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run_30_05_2018_t_19_22_40/result_1_pita_targets_

# pita_prediction.pl \
# -utr /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
# -mir /nethome/mct30/bmds/miRDeep2/mirdeep_runs/3_run_23_08_2018_t_20_16_13/animal_miRNAs.fa \
# -gxp -gu 0 \
# -prefix /nethome/mct30/bmds/miRDeep2/mirdeep_runs/3_run_23_08_2018_t_20_16_13/animal_miRNAs_pita_targets

pita_prediction.pl \
-utr /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref_three_prime_utr.fasta \
-mir /nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique.fa \
-gxp -gu "6;0,7;0,8;0" -m "6;0,7;0,8;0" \
-prefix /nethome/mct30/bmds/miR-PREFeR_predictions_10X_20-24_300_2/target_prediction/pita/G006_Gut_F_trimmed_17-35_plants_miRNA.mature_good_unique_targets

# gu: no G:U wobble in 6nt seeds or 7nt seecs or 8nt seeds
# m same as above for mismatches