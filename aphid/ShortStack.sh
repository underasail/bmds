#! /bin/bash

ShortStack \
--readfile /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta \
--outdir /nethome/mct30/bmds/ShortStack_5X_17-35_inclusion \
--genomefile /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion.fasta \
--bowtie_cores 1 --mincov 10 --dicermin 17 --dicermax 35 --foldsize 700 --mmap f

# /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion.fasta