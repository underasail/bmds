#! /bin/bash

#BSUB -J G006_pipline
#BSUB -e /nethome/mct30/err/G006_pipline.err
#BSUB -o /nethome/mct30/out/G006_pipline.out
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

module switch python/3.3.1
# need to work in python3

module load bowtie2
# need to load bowtie2 from /share


#
# G006
#

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G006_Bac_Buchnera.map \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G006 bacteriocyte reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus

/nethome/mct30/gitclones/bmds/aphid/elimMatched.py \
/nethome/mct30/bmds/SAM_out/G006_Gut_Buchnera.map \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35.fa \
/nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta
# Builds new FASTA file for G006 gut reads that didn't perfectly
# align to reference genomes for Buchnera and/or Myzus



#
# G006 Plants
#

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
-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Bac_plants.map
# G006 bacteriocyte reads aligned against the plants

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/plants/plants_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_plants.map
# G006 gut reads aligned against the plants


#
# G006 Other Bacteria
#

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
-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Bac_other_bacteria.map
# G006 bacteriocyte reads aligned against the other_bacteria

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/other_bacteria/other_bacteria_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_other_bacteria.map
# G006 gut reads aligned against the other_bacteria


#
# G006 Viruses
#

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
-U /nethome/mct30/bmds/reads/G006_Bac_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Bac_viruses.map
# G006 bacteriocyte reads aligned against the viruses

/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/viruses/viruses_index \
-U /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_unmatched.fasta \
-S /nethome/mct30/bmds/SAM_out/G006_Gut_viruses.map
# G006 gut reads aligned against the viruses




#
# Percentage Calculations
#

for filename in /nethome/mct30/bmds/SAM_out/*.map; do
    /nethome/mct30/gitclones/bmds/aphid/perSAM.py \
    $filename;
done
