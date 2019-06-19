#! /bin/bash

#BSUB -J bowtie2_other_bacteria_viruses_plant_alignments
#BSUB -e /nethome/mct30/err/bowtie2_other_bacteria_viruses_plant_alignments_3.err
#BSUB -o /nethome/mct30/out/bowtie2_other_bacteria_viruses_plant_alignments_3.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
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

# bowtie2-build -f \
# /nethome/mct30/bmds/index/plant_precursors/exact_mirs_precursors.fasta \
# /nethome/mct30/bmds/index/plant_precursors/plant_precursors_index


parallel --link --eta \
"bowtie2 -L 10 -f -p 8 --no-unal \
-a \
-x /nethome/mct30/bmds/index/plant_precursors/plant_precursors_index \
-U /nethome/mct30/bmds/reads/{2}_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/{1}_plants_a_all-reads.map" \
::: G006_Gut G002_Gut BTIRed_Gut \
G006_Bac G002_Bac BTIRed_Bac \
::: G006_Gut_F G002_Gut BTIRed_Gut \
G006_Bac_F G002_Bac BTIRed_Bac

# #
# # G002 Plants
# #

# export filelist=''
# for filename in /nethome/mct30/bmds/ref_genomes/plants/*.fasta; do
#     filelist+=$filename;
#     filelist+=',';
# done

# /share/apps/bowtie2/2.2.6/bowtie2-build -f \
# $filelist \
# /nethome/mct30/bmds/index/plants/plants_index
# # Building an index for the plant

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/G002_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Bac_plants.map
# # -L 10 (seed length) -f (FASTA format for reads), 
# # -p 4 (number of parallel search threads on separate cores), 
# # --no-unal (doesn't record unaligned reads), -x (index files' basename), 
# # -U (reads FASTA file), -S (SAM file output)
# # G002 bacteriocyte reads aligned against the plants

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/G002_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Gut_plants.map
# # G002 gut reads aligned against the plants


# #
# # G006 Plants
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/G006_Bac_F_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Bac_plants.map
# # G006 bacteriocyte reads aligned against the plants

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/G006_Gut_F_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Gut_plants.map
# # G006 gut reads aligned against the plants


# #
# # BTIRed Plants
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_plants.map
# # BTIRed bacteriocyte reads aligned against the plants

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/plants/plants_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_plants.map
# # BTIRed gut reads aligned against the plants


# #
# # G002 Other Bacteria
# #

# export filelist=''
# for filename in /nethome/mct30/bmds/ref_genomes/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/*.fna; do
#     filelist+=$filename;
#     filelist+=',';
# done

# /share/apps/bowtie2/2.2.6/bowtie2-build -f \
# $filelist \
# /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index
# # Building an index for the other bacteria

# export filelist=''
# for filename in /nethome/mct30/bmds/ref_genomes/CRi-5.15/*.fna; do
#     filelist+=$filename;
#     filelist+=',';
# done

# /share/apps/bowtie2/2.2.6/bowtie2-build -f \
# $filelist \
# /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index
# # Building an index for the other bacteria

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/G002_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Bac_other_bacteria_HF_2018_corrected.map
# # G002 bacteriocyte reads aligned against the other_bacteria

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/G002_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Gut_other_bacteria_HF_2018_corrected.map
# # G002 gut reads aligned against the other_bacteria


# #
# # G006 Other Bacteria
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/G006_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Bac_other_bacteria_HF_2018_corrected.map
# # G006 bacteriocyte reads aligned against the other_bacteria

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/G006_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Gut_other_bacteria_HF_2018_corrected.map
# # G006 gut reads aligned against the other_bacteria


# #
# # BTIRed Other Bacteria
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_other_bacteria_HF_2018_corrected.map
# # BTIRed bacteriocyte reads aligned against the other_bacteria

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper/other-bacteria_HF-lit-search_and_2018-aphid-gut-paper_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_other_bacteria_HF_2018_corrected.map
# # BTIRed gut reads aligned against the other_bacteria

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/G006_Bac_CRi.map

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/G006_Gut_CRi.map

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/G002_Bac_CRi.map

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/G002_Gut_CRi.map

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Bac_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_CRi.map

# /share/apps/bowtie2/2.2.6/bowtie2 -L10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/CRi-5.15/CRi-5.15_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Gut_trimmed_17-35.fa \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_CRi.map


# #
# # G002 Viruses
# #

# export filelist=''
# for filename in /nethome/mct30/bmds/ref_genomes/viruses2/*.fna; do
#     filelist+=$filename;
#     filelist+=',';
# done

# /share/apps/bowtie2/2.2.6/bowtie2-build -f \
# $filelist \
# /nethome/mct30/bmds/index/viruses2/viruses2_index
# # Building an index for the Viruses



# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/G002_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Bac_viruses2_corrected.map
# # G002 bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/G002_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Gut_viruses2_corrected.map
# # G002 gut reads aligned against the viruses



# #
# # G006 Viruses
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/G006_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Bac_viruses2_corrected.map
# # G006 bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/G006_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Gut_viruses2_corrected.map
# # G006 gut reads aligned against the viruses


# #
# # BTIRed Viruses
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_viruses2_corrected.map
# # BTIRed bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses2/viruses2_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_viruses2_corrected.map
# BTIRed gut reads aligned against the viruses


# #
# # G002 Viruses
# #

# export filelist=''
# for filename in /nethome/mct30/bmds/ref_genomes/viruses/*.fasta; do
#     filelist+=$filename;
#     filelist+=',';
# done

# /share/apps/bowtie2/2.2.6/bowtie2-build -f \
# $filelist \
# /nethome/mct30/bmds/index/viruses/viruses_index
# # Building an index for the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/G002_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Bac_viruses.map
# # G002 bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/G002_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G002_Gut_viruses.map
# # G002 gut reads aligned against the viruses


# #
# # G006 Viruses
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/G006_Bac_F_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Bac_viruses.map
# # G006 bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/G006_Gut_F_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/G006_Gut_viruses.map
# # G006 gut reads aligned against the viruses


# #
# # BTIRed Viruses
# #

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Bac_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Bac_viruses.map
# # BTIRed bacteriocyte reads aligned against the viruses

# /share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 4 --no-unal \
# -x /nethome/mct30/bmds/index/viruses/viruses_index \
# -U /nethome/mct30/bmds/reads/BTIRed_Gut_unmatched_corrected.fasta \
# -S /nethome/mct30/bmds/SAM_out/BTIRed_Gut_viruses.map
# # BTIRed gut reads aligned against the viruses



#
# File Structure
#

# /nethome/mct30/bmds/
# ├ index
# │   ├ plants
# │   ├ other_bacteria
# │   ├ viruses
# │   ├ BTIRed-Buchnera
# │   ├ G002-Buchnera
# │   ├ G006-Buchnera
# │   ├ BTIRed-Myzus
# │   ├ G002-Myzus
# │   ├ G006-Myzus
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
# │   ├ G006-Myzus
# │   ├ BTIRed
# │   ├ G002
# │   ├ BTIRed_Buchnera_genome_ref.fasta
# │   ├ BTIRed_Buchnera_pLeu_ref.fasta
# │   ├ G002_Buchnera_genome_ref.fasta
# │   ├ G002_Buchnera_pLeu_ref.fasta
# │   ├ G006_Buchnera_1genome_ref.fasta
# │   ├ G006_Buchnera_2genome_ref.fasta
# │   └ G006_Myzus_genome_ref.fasta
# └ SAM_out
