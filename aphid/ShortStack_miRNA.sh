#! /bin/bash

ShortStack \
--bowtie_cores 8 \
--sort_mem 30000M \
--outdir \
/nethome/mct30/acypi/sra/plants/ShortStack_0.25rpmm_20-24_f_300_SRA_ca27_q28_17-25 \
--genomefile /nethome/mct30/acypi/sra/plants/GCF_000695525.1_BOL_genomic.fasta \
--readfile \
/nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27_SRR799356-58_vdb_cutad_q28_17-25.fasta
--mmap f \
--dicermin 20 \
--dicermax 24 \
--foldsize 300 \
--mincov 16

# --mincov 16 from q28_17-25
# --mincov 0.25rpmm

# --bamfile \
# nethome/mct30/acypi/sra/plants/SRR799356-58_vdb_cutad_q28_17-25.bam \
# --total_primaries 63067395 \

# --readfile /nethome/mct30/acypi/sra/plants/SRR799356-58_vdb_cutad_q28_17-25.fasta \
# --strand_cutoff 0.7 \
# --pad 25
# --bamfile /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_q28.bam \
# --readfile /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_q28.fasta \
# --bamfile /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27.bam \
# --readfile /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27.fasta \
# --readfile /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta \
# --genomefile /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
# --bamfile \
# /nethome/mct30/bmds/ShortStack_5X_17-35_u_showsec/G006_Gut_F_trimmed_17-35_plants.bam \
# --genomefile /nethome/mct30/acypi/sra/plants/GCF_000695525.1_BOL_genomic.fasta \

# /ShortStack_0.25rpmm_20-24_f_300_SRA-ca27/MIRNAs