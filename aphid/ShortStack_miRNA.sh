#! /bin/bash

ShortStack \
--readfile /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta \
--outdir /nethome/mct30/bmds/ShortStack_5X_17-35_u_showsec \
--genomefile /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
--bowtie_cores 8 \
--mincov 5 \
--dicermin 17 \
--dicermax 35 \
--foldsize 700 \
--show_secondaries \
--mmap u