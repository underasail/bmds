#! /bin/bash

ShortStack \
--readfile /scratch/projects/acypi/sra/SRR6517745.fasta \
--outdir /nethome/mct30/bmds/ShortStack_10X_20-24_u_300_showsec_sra \
--genomefile \
/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
--bowtie_cores 4 \
--mincov 10 \
--dicermin 20 \
--dicermax 24 \
--foldsize 300 \
--show_secondaries \
--sort_mem 8500M \
--mmap u

# --readfile /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta \
# --genomefile /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
# --bamfile \
# /nethome/mct30/bmds/ShortStack_5X_17-35_u_showsec/G006_Gut_F_trimmed_17-35_plants.bam \