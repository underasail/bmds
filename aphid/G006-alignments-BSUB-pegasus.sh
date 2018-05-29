#! /bin/bash

#BSUB -J G006-bowtie2_Buch_Myz_plant_split_alignments
#BSUB -e /nethome/mct30/err/G006-bowtie2_Buch_Myz_plant_split_alignments.err
#BSUB -o /nethome/mct30/out/G006-bowtie2_Buch_Myz_plant_split_alignments.out
#BSUB -n 16
#BSUB -P acypi
#BSUB -R "span[ptile=16]"
#BSUB -q parallel
#BSUB -W 72:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores, queue, run time limit, 
# send email when jobs begins, send email with stats when job finished, email,
# default RAM per core is 1500MB

module load bowtie2
# Need to load bowtie2 module from /share


############################################
# G006 Gut and Bacteriocyte Alignments for #
# Myzus, Buchnera, and Plant Individually  #
############################################

# parallel --link -j 6 \
# 'bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
# -x /nethome/mct30/bmds/index/{1}/{1}_index \
# -U /nethome/mct30/bmds/reads/{2} \
# -S /nethome/mct30/bmds/SAM_out/{3}' \
# ::: G006-Myzus G006-Myzus G006-Buchnera G006-Buchnera plants plants \
# ::: G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
# G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
# G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
# ::: G006_Bac_Myzus-only.map G006_Gut_Myzus-only.map \
# G006_Bac_Buchnera-only.map G006_Gut_Buchnera-only.map \
# G006_Bac_plants-only.map G006_Gut_plants-only.map

parallel --link -j 2 \
'bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
-x /nethome/mct30/bmds/index/G006/G006_Buchnera_Myzus_plant_index \
-U /nethome/mct30/bmds/reads/{1} \
-S /nethome/mct30/bmds/SAM_out/{2}' \
::: G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
::: G006_Bac_Buchnera_Myzus_plant.map G006_Gut_Buchnera_Myzus_plant.map