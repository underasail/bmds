#! /bin/bash

#BSUB -J G006-bowtie2_Buch_Myz_plant_split_alignments
#BSUB -e /nethome/mct30/err/G006-bowtie2_Buch_Myz_plant_split_alignments.err
#BSUB -o /nethome/mct30/out/G006-bowtie2_Buch_Myz_plant_split_alignments.out
#BSUB -n 48
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

##############
# G006 Myzus #
##############

# Myzus index is the same as the one for G002 reads

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/G006-Myzus/G006_Myzus_index \
#-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Bac_Myzus-only.map
# G006 bacteriocyte reads aligned against G006 Myzus

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/G006-Myzus/G006_Myzus_index \
#-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Gut_Myzus-only.map
# G006 gut reads aligned against G006 Myzus

#################
# G006 Buchnera #
#################

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/G006-Buchnera/G006_Buchnera_index \
#-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Bac_Buchnera-only.map
# G006 bacteriocyte reads aligned against G006 Buchnera (genome parts 1 and 2)

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/G006-Buchnera/G006_Buchnera_index \
#-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Gut_Buchnera-only.map
# G006 gut reads aligned against G006 Buchnera (genome parts 1 and 2)

###############
# G006 Plants #
###############

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/plants/plants_index \
#-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Bac_plants-only.map
# G006 bacteriocyte reads aligned against the plants

#/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
#-x /nethome/mct30/bmds/index/plants/plants_index \
#-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
#-S /nethome/mct30/bmds/SAM_out/G006_Gut_plants-only.map
# G006 gut reads aligned against the plants

############
# Parallel #
############

parallel --link -j 6 \
'bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
-x /nethome/mct30/bmds/index/{1}/{1}_index \
-U /nethome/mct30/bmds/reads/{2} \
-S /nethome/mct30/bmds/SAM_out/{3}' \
::: G006-Myzus G006-Myzus G006-Buchnera G006-Buchnera plants plants \
::: G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
G006_Bac_F_trimmed_17-35.fa G006_Gut_F_trimmed_17-35.fa \
::: G006_Bac_Myzus-only.map G006_Gut_Myzus-only.map \
G006_Bac_Buchnera-only.map G006_Gut_Buchnera-only.map \
G006_Bac_plants-only.map G006_Gut_plants-only.map