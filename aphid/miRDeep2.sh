#! /bin/bash

#BSUB -J miRDeep2
#BSUB -e /nethome/mct30/err/miRDeep2_9.err
#BSUB -o /nethome/mct30/out/miRDeep2_9.out
#BSUB -n 1
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

# module load bowtie

mkdir -p /nethome/mct30/bmds/index/bt1-plant

# export PERL5LIB=$PERL5LIB:/nethome/mct30/perl5/lib/perl5/x86_64-linux-thread-multi/Compress/Raw:/nethome/mct30/perl5/lib/perl5/x86_64-linux-thread-multi:/nethome/mct30/perl5/lib/perl5:/nethome/mct30/gitclones/mirdeep2/lib/perl5/x86_64-linux-thread-multi:/nethome/mct30/gitclones/mirdeep2/lib/perl5:/usr/local/lib64/perl5:/usr/local/share/perl5:/usr/lib64/perl5/vendor_perl:/usr/share/perl5/vendor_perl:/usr/lib64/perl5:/usr/share/perl5

cd /nethome/mct30/bmds/miRDeep2/

# /nethome/mct30/gitclones/mirdeep2/essentials/bowtie-1.1.1/bowtie-build \
# -f /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
# /nethome/mct30/bmds/index/bt1-plant/bt1-plant-index
# # Builds bowtie1 index for noheader fasta

# /nethome/mct30/gitclones/mirdeep2/bin/mapper.pl \
# /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta -c \
# -i -j -m \
# -s /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed_2.fasta
# # Takes Myzus only filtered reads and collapses redundancy while renaming reads

# /nethome/mct30/gitclones/mirdeep2/bin/mapper.pl \
# /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed_2.fasta -c \
# -i -j -p /nethome/mct30/bmds/index/bt1-plant/bt1-plant-index \
# -t /nethome/mct30/bmds/plant/G006_Gut_F_trimmed_17-35_plant_collapsed_2_vs_genome.arf
# # produces arf mapped output with no mismatches from collapsed reads

# # There is an error produced when using these two together. count2 isn't set well
# # If doing separately, need to carry the collapsed reads over as the input to generate
# # the arf file

/nethome/mct30/gitclones/mirdeep2/bin/miRDeep2.pl \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed_2.fasta \
/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
/nethome/mct30/bmds/plant/G006_Gut_F_trimmed_17-35_plant_collapsed_2_vs_genome.arf \
/nethome/mct30/bmds/plant/bol_miRNAs.fa \
none \
none
# Path to program
# Input miRDeep2 collapsed FASTA reads file
# Input genome FASTA with no whitespaces in header
# Input ARF file with 'seq_x' before each read number 
#     sed "s/^/seq_x/" ~/bmds/G006_Gut_mapped.arf > 
#     ~/bmds/G006_Gut_mapped_seqreadid.arf
# Input file of known Mpe miRNAs
# Input file of miRNAs from A pisum
# Input file of known Mpe miRNA precursors

# perl /nethome/mct30/gitclones/mirdeep2/bin/make_html.pl \
# -f /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run*/output.mrd \
# -s /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run*/survey.csv \
# -c -y 
# # creates output csv, html, and pdf files