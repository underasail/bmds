#! /bin/bash

#BSUB -J bowtie2-indexing
#BSUB -e /scratch/projects/acypi/err/bowtie2-indexing.err
#BSUB -o /scratch/projects/acypi/out/bowtie2-indexing.out
#BSUB -n 7
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

module load bowtie2

parallel --link \
'export filelist=
for filename in /nethome/mct30/bmds/ref_genomes/{}/*.fasta; do
    filelist+=$filename;
    filelist+=",";
done

bowtie2-build -f \
$filelist \
/nethome/mct30/bmds/index/{}/{}_index' \
::: plants viruses other_bacteria G006-Myzus G006-Buchnera \
G002-Buchnera BTIRed-Buchnera

# parallel --link \
# "bowtie2-build -f \
# /nethome/mct30/bmds/ref_genomes/{}-Buchnera/{}_Buchnera_genome_ref.fasta,\
# /nethome/mct30/bmds/ref_genomes/G006-Myzus/G006_Myzus_genome_ref.fasta \
# /nethome/mct30/bmds/index/{}/{}_Buchnera_Myzus_index" \
# ::: G002 G006 BTIRed
