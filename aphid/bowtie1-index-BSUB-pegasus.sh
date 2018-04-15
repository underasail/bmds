#! /bin/bash

#BSUB -J bt1-index
#BSUB -e /nethome/mct30/err/bt1-index.err
#BSUB -o /nethome/mct30/out/bt1-index.out
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

module load bowtie

bowtie-build -f \
/nethome/mct30/bmds/ref_genomes/plants/single/plant_genome.fasta \
/nethome/mct30/bmds/index/bt1-plant/plant
# Path to bowtie-build from mirdeep2 bowtie1 install
# Plant reference genome
# Path to index directory