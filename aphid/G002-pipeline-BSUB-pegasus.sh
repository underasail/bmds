#! /bin/bash

#BSUB -J G002_pipline
#BSUB -e /nethome/mct30/err/G002_pipline.err
#BSUB -o /nethome/mct30/out/G002_pipline.out
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

module switch python/3.3.1 > /dev/null 2>&1
# need to work in python3

module load bowtie2
# need to load bowtie2 from /share


###########################################
# G002 Myzus/Buchnera Together Alignments #
###########################################

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
/nethome/mct30/bmds/ref_genomes/G002_Buchnera_genome_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G002_Buchnera_pLeu_ref.fasta,\
/nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref.fasta \
/nethome/mct30/bmds/index/G002/G002_Buchnera_Myzus_index
# Building an index for the G002 line using the genome and plasmid sections of the G002 genome
# as well as the G006 Myzus genome

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G002/G002_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_Buchnera.map
# G002 bacteriocyte reads aligned against G002 Buchnera (genome and plasmid)
# and G006 Myzus (genome)

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/G002/G002_Buchnera_Myzus_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_Buchnera.map
# G002 gut reads aligned against G002 Buchnera (genome and plasmid)
# and G006 Myzus (genome)


#################################
# G002 Unmatched FASTA Creation #
#################################

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G002_Bac_Buchnera.map \
/nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G002 bacteriocyte reads that didn't
# align to reference genomes for Buchnera and/or Myzus

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G002_Gut_Buchnera.map \
/nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G002 gut reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus


##########################
# G002 Plants Alignments #
##########################

export filelist=''
for filename in /nethome/mct30/bmds/ref_genomes/plants/*.fasta; do
    filelist+=$filename;
    filelist+=',';
done

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
$filelist \
/nethome/mct30/bmds/index/plants/plants_index
# Building an index for the plant

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_plants.map
# G002 bacteriocyte reads aligned against the plants

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_plants.map
# G002 gut reads aligned against the plants


##################################
# G002 Other Bacteria Alignments #
##################################

export filelist=''
for filename in /nethome/mct30/bmds/ref_genomes/other_bacteria/*.fasta; do
    filelist+=$filename;
    filelist+=',';
done

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
$filelist \
/nethome/mct30/bmds/index/other_bacteria/other_bacteria_index
# Building an index for the other bacteria

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/other_bacteria/other_bacteria_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_other_bacteria.map
# G002 bacteriocyte reads aligned against the other_bacteria

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/other_bacteria/other_bacteria_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_other_bacteria.map
# G002 gut reads aligned against the other_bacteria


###########################
# G002 Viruses Alignments #
###########################

export filelist=''
for filename in /nethome/mct30/bmds/ref_genomes/viruses/*.fasta; do
    filelist+=$filename;
    filelist+=',';
done

/share/apps/bowtie2/2.2.6/bowtie2-build -f \
$filelist \
/nethome/mct30/bmds/index/viruses/viruses_index
# Building an index for the viruses

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/viruses/viruses_index \
-U /nethome/mct30/bmds/reads/G002_Bac_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Bac_viruses.map
# G002 bacteriocyte reads aligned against the viruses

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/viruses/viruses_index \
-U /nethome/mct30/bmds/reads/G002_Gut_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G002_Gut_viruses.map
# G002 gut reads aligned against the viruses


################################
# G002 Percentage Calculations #
################################

cd /nethome/mct30/bmds/SAM_out/
for filename in G002*Buchnera.map; do
    /nethome/mct30/gitclones/bmds/aphid/perSAM.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done
# Gets percentage of matched reads for Buchnera and Myzus genomes


##############################################
# Percentage for G002 Other Bacteria Genomes #
##############################################

for filename in G002*other_bacteria.map; do
    /nethome/mct30/gitclones/bmds/aphid/perGenomes.py \
    /nethome/mct30/bmds/SAM_out/$filename \
    /nethome/mct30/gitclones/bmds/aphid/files/$filename.tsv
done
# Gets percentage of unmatched reads that match to other bacteria
