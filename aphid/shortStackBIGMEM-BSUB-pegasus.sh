#! /bin/bash

#BSUB -J ShortStackBIGMEM
#BSUB -e /nethome/mct30/err/ShortStackBIGMEM.err
#BSUB -o /nethome/mct30/out/ShortStackBIGMEM.out
#BSUB -n 64
#BSUB -R "span[ptile=16]"
#BSUB -R "rusage[mem=3800]"
#BSUB -q bigmem
#BSUB -P acypi
#BSUB -W 115:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module load bowtie samtools

ShortStack \
--readfile /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta \
--outdir /nethome/mct30/bmds/ShortStackBIGMEM \
--genomefile /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
--bowtie_cores 64 \
--sort_mem 3795M
