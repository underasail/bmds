#! /bin/bash

#BSUB -J G002_alignments
#BSUB -e /nethome/mct30/err/G002_alignments.err
#BSUB -o /nethome/mct30/out/G002_alignments.out
#BSUB -n 6
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

module load bowtie2

parallel --link -j 6 \
'bowtie2 -L 10 -f -p 8 --no-unal --no-hd \
-x /nethome/mct30/bmds/index/{1}/{1}_index \
-U /nethome/mct30/bmds/reads/{2} \
-S /nethome/mct30/bmds/SAM_out/{3}' \
::: G006-Myzus G006-Myzus G002-Buchnera G002-Buchnera plants plants \
::: G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
G002_Bac_trimmed_17-35.fa G002_Gut_trimmed_17-35.fa \
::: G002_Bac_Myzus-only.map G002_Gut_Myzus-only.map \
G002_Bac_Buchnera-only.map G002_Gut_Buchnera-only.map \
G002_Bac_plants-only.map G002_Gut_plants-only.map
