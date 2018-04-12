#! /bin/bash

#BSUB -J mirdeep2_gut_myzus
#BSUB -e /nethome/mct30/err/mirdeep2_gut_myzus.err
#BSUB -o /nethome/mct30/out/mirdeep2_gut_myzus.out
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

cd /nethome/mct30/bmds/miRDeep2
# so the mapper_logs and runs folders are in a good place

#/nethome/mct30/gitclones/mirdeep2/essentials/bowtie-1.1.1/bowtie-build \
#-f /nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_noheader.fasta \
#/nethome/mct30/bmds/index/bt1-G006-Myzus/bt1-G006-Myzus-index
# Builds bowtie1 index for noheader fasta

/nethome/mct30/gitclones/mirdeep2/bin/mapper.pl \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa -c \
-i -j -m \
-p /nethome/mct30/bmds/index/bt1-G006-Myzus/bt1-G006-Myzus-index \
-s /nethome/mct30/bmds/reads/G006_Gut_collapsed.fa \
-t /nethome/mct30/bmds/ref_genomes/G006_Gut_collapsed_Myzus_mapped.arf
# Collapses G006 gut reads and maps them to the Myzus genome

/nethome/mct30/gitclones/mirdeep2/bin/miRDeep2.pl \
/nethome/mct30/bmds/reads/G006_Gut_collapsed.fa \
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_noheader.fasta \
/nethome/mct30/bmds/ref_genomes/G006_Gut_collapsed_Myzus_mapped.arf \
/nethome/mct30/bmds/Mpe_miRNAs_mature.fa \
/nethome/mct30/bmds/api_miRNAs.fa none
# Does predictions

/nethome/mct30/local/perl/bin/perl \
/nethome/mct30/gitclones/mirdeep2/bin/make_html.pl \
-f /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run*/output.mrd \
-s /nethome/mct30/bmds/miRDeep2/mirdeep_runs/run*/survey.csv \
-c -y 2
# creates output csv, html, and pdf files