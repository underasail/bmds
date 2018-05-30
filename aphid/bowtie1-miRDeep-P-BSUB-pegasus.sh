#! /bin/bash

#BSUB -J bt1-miRDeep-P
#BSUB -e /nethome/mct30/err/bt1-miRDeep-P.err
#BSUB -o /nethome/mct30/out/bt1-miRDeep-P.out
#BSUB -n 8
#BSUB -q general
#BSUB -W 72:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module load bowtie samtools

mkdir -p /nethome/mct30/bmds/index/bt1-plant

bowtie-build -f \
/nethome/mct30/bmds/ref_genomes/plants/GCA_000604025.1_BOL_v1.0_genomic.fasta \
/nethome/mct30/bmds/index/bt1-plant/plant
# Path to bowtie-build from mirdeep2 bowtie1 install
# Plant reference genome
# Path to index directory

/nethome/mct30/gitclones/mirdeep2/bin/mapper.pl \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta -c \
-j -m -s /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed.fasta

bowtie --threads 8 -a -v 0 /nethome/mct30/bmds/index/bt1-plant/plant \
-f /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed.fasta \
>/nethome/mct30/bmds/plant/G006_Gut_plant.aln
# miRDeep-P requires perfect alignments

/nethome/mct30/local/mirDeep-P/miRDP1.3/convert_bowtie_to_blast.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant.aln \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed.fasta \
/nethome/mct30/bmds/ref_genomes/plants/GCA_000604025.1_BOL_v1.0_genomic.fasta \
>/nethome/mct30/bmds/plant/G006_Gut_plant.bst

/nethome/mct30/local/mirDeep-P/miRDP1.3/filter_alignments.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant.bst -c 20 \
>/nethome/mct30/bmds/plant/G006_Gut_plant_filter20.bst
# -c sets cutoff for larget miRNA family
# 14 in Arabidopsis, not sure for this plant

/nethome/mct30/local/mirDeep-P/miRDP1.3/overlap.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant_filter20.bst \
/nethome/mct30/bmds/plant/B.oleracea_v1.0_ncRNA.gff -b \
>/nethome/mct30/bmds/plant/id_overlap_ncRNA_B.oleracea
# ncRNA gffs sourced from http://www.ocri-genomics.org/bolbase/login.htm
# Help > Downloads

/nethome/mct30/local/mirDeep-P/miRDP1.3/alignedselected.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant_filter20.bst -g \
/nethome/mct30/bmds/plant/id_overlap_ncRNA_B.oleracea \
>/nethome/mct30/bmds/plant/G006_Gut_plant_filter20_ncRNA_B.oleracea.bst

/nethome/mct30/local/mirDeep-P/miRDP1.3/filter_alignments.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant_filter20_ncRNA_B.oleracea.bst -b \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed.fasta \
> /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed_filtered.fa

/nethome/mct30/local/mirDeep-P/miRDP1.3/excise_candidate.pl \
/nethome/mct30/bmds/ref_genomes/plants/GCA_000604025.1_BOL_v1.0_genomic.fasta \
/nethome/mct30/bmds/plant/G006_Gut_plant_filter20_ncRNA_B.oleracea.bst 250 \
>/nethome/mct30/bmds/plant/G006_Gut_plant_precursors.fa

cat /nethome/mct30/bmds/plant/G006_Gut_plant_precursors.fa \
| /nethome/mct30/local/ViennaRNA/bin/RNAfold --noPS \
> /nethome/mct30/bmds/plant/G006_Gut_plant_structures

bowtie-build -f /nethome/mct30/bmds/plant/G006_Gut_plant_precursors.fa \
/nethome/mct30/bmds/index/bt1-plant-precursors/G006_Gut_plant_precursors

bowtie --threads 8 -a -v 0 \
/nethome/mct30/bmds/index/bt1-plant-precursors/G006_Gut_plant_precursors \
-f /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed.fasta \
> /nethome/mct30/bmds/plant/G006_Gut_plant_precursors.aln

/nethome/mct30/local/mirDeep-P/miRDP1.3/convert_bowtie_to_blast.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant_precursors.aln \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants_collapsed_filtered.fa \
/nethome/mct30/bmds/plant/G006_Gut_plant_precursors.fa \
> /nethome/mct30/bmds/plant/G006_Gut_plant_precursors.bst

sort +3 -25 /nethome/mct30/bmds/plant/G006_Gut_plant_precursors.bst \
> /nethome/mct30/bmds/plant/G006_Gut_plant_signatures

/nethome/mct30/local/mirDeep-P/miRDP1.3/miRDP.pl \
/nethome/mct30/bmds/plant/G006_Gut_plant_signatures \
/nethome/mct30/bmds/plant/G006_Gut_plant_structures \
> /nethome/mct30/bmds/plant/G006_Gut_plant_predictions

samtools faidx /nethome/mct30/bmds/ref_genomes/plants/GCA_000604025.1_BOL_v1.0_genomic.fasta
cut -f1,2 /nethome/mct30/bmds/ref_genomes/plants/GCA_000604025.1_BOL_v1.0_genomic.fasta.fai \
> /nethome/mct30/bmds/plant/plant.chrom.sizes
# https://www.biostars.org/p/173963/#174150

/nethome/mct30/local/mirDeep-P/miRDP1.3/rm_redundant_meet_plant.pl \
/nethome/mct30/bmds/plant/plant.chrom.sizes \
/nethome/mct30/bmds/plant/G006_Gut_plant_precursors.fa \
/nethome/mct30/bmds/plant/G006_Gut_plant_predictions \
/nethome/mct30/bmds/plant/G006_Gut_plant_nr_prediction \
/nethome/mct30/bmds/plant/G006_Gut_plant_filter_P_prediction
# nr_prediction: contains non-redundant predicted miRNA information
# _P_prediction: contains predicted miRNAs that meet the criteria of plant miRNAs
# Format details are in Section 6 of the manual
