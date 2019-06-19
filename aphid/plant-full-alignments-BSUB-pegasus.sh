#! /bin/bash

#BSUB -J plant_full_alignments
#BSUB -e /nethome/mct30/err/plant_full_alignments.err
#BSUB -o /nethome/mct30/err/plant_full_alignments.out
#BSUB -n 8
#BSUB -q general
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

bowtie2 -L 10 -f -p 8 --no-unal \
-a -R 10 
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_plants-full.map


#
# G002 Plants
#

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_plants-full.map
# -L 10 (seed length) -f (FASTA format for reads), 
# -p 8 (number of parallel search threads on separate cores), 
# --no-unal (doesn't record unaligned reads), -x (index files' basename), 
# -U (reads FASTA file), -S (SAM file output)
# G002 bacteriocyte reads aligned against the plants

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_plants-full.map
# G002 gut reads aligned against the plants


#
# G006 Plants
#

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G006_Bac_plants-full.map
# G006 bacteriocyte reads aligned against the plants

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_plants-full.map
# G006 gut reads aligned against the plants


#
# BTIRed Plants
#

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/BTIRed_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_plants-full.map
# BTIRed bacteriocyte reads aligned against the plants

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/BTIRed_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_plants-full.map
# BTIRed gut reads aligned against the plants