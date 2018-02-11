#! /bin/bash

#BSUB -J bowtie2_Buch_Myz_alignments
#BSUB -e /nethome/mct30/bowtie2_Buch_Myz_alignments.err
#BSUB -o /nethome/mct30/bowtie2_Buch_Myz_alignments.out
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

#
# G002
#

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
/nethome/mct30/bmds/ref_genomes/G002_Buchnera_genome_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G002_Buchnera_pLeu_ref.fasta,\
/nethome/mct30/bmds/index/G002-Buchnera/G002_Buchnera_index
# Building an index for the G002 line using the G002 genome and pLeu plasmid

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G002-Buchnera/G002_Buchnera_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_Buchnera-only.map
# -L 10 (seed length) -f (FASTA format for reads), 
# -p 8 (number of parallel search threads on separate cores), 
# --no-unal (doesn't record unaligned reads), -x (index files' basename), 
# -U (reads FASTA file), -S (SAM file output)
# G002 bacteriocyte reads aligned against G002 Buchnera (genome and plasmid)

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G002-Buchnera/G002_Buchnera_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_Buchnera-only.map
# G002 gut reads aligned against G002 Buchnera (genome and plasmid)

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref.fasta
/nethome/mct30/bmds/index/G006-Myzus/G006_Myzus_index
# Building an index for G006 Myzus

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G006-Myzus/G006_Myzus_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_Myzus-only.map
# G002 bacteriocyte reads aligned against G006 Myzus

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G006-Myzus/G006_Myzus_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_Myzus-only.map
# G002 gut reads aligned against G006 Myzus


#
# G006
#

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
/nethome/mct30/bmds/ref_genomes/G006_Buchnera_1genome_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G006_Buchnera_2genome_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref.fasta \
/nethome/mct30/bmds/index/G006/G006_Buchnera_Myzus_index
# Building an index for the G006 line using the two sections of the G006 genome
# as well as the G006 Myzus genome

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G006/G006_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G006_Bac_Buchnera.map
# G006 bacteriocyte reads aligned against G006 Buchnera (genome parts 1 and 2)
# and G006 Myzus (genome)

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G006/G006_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_Buchnera.map
# G006 gut reads aligned against G006 Buchnera (genome parts 1 and 2)
# and G006 Myzus (genome)


#
# BTIRed
#

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
/nethome/mct30/bmds/ref_genomes/BTIRed_Buchnera_genome_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/BTIRed_Buchnera_pLeu_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref.fasta \
/nethome/mct30/bmds/index/BTIRed/BTIRed_Buchnera_Myzus_index
# Building an index for the BTIRed line using BTIRed genome and pLeu plasmid
# as well as the G006 Myzus genome

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/BTIRed/BTIRed_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/BTIRed_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_Buchnera.map
# BTIRed bacteriocyte reads aligned against BTIRed Buchnera (genome and pLeu plasmid)
# and G006 Myzus (genome)

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/BTIRed/BTIRed_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/BTIRed_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_Buchnera.map
# BTIRed gut reads aligned against BTIRed Buchnera (genome and pLeu plasmid)
# and G006 Myzus (genome)


#
# File Structure
#

# /nethome/mct30/bmds/
# ├ index
# │   ├ BTIRed
# │   ├ G002
# │   └ G006
# ├ reads
# │   ├ BTIRed_Bac_trimmed_17-35.fa
# │   ├ BTIRed_Gut_trimmed_17-35.fa
# │   ├ G002_Bac_trimmed_17-35.fa
# │   ├ G002_Gut_trimmed_17-35.fa
# │   ├ G006_Bac_F_trimmed_17-35.fa
# │   └ G006_Gut_F_trimmed_17-35.fa
# ├ ref_genomes
# │   ├ BTIRed_Buchnera_genome_ref.fasta
# │   ├ BTIRed_Buchnera_pLeu_ref.fasta
# │   ├ G002_Buchnera_genome_ref.fasta
# │   ├ G002_Buchnera_pLeu_ref.fasta
# │   ├ G006_Buchnera_1genome_ref.fasta
# │   ├ G006_Buchnera_2genome_ref.fasta
# │   └ G006_Myzus_genome_ref.fasta
# └ SAM_out
