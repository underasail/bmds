#! /bin/bash

#BSUB -J b2-align
#BSUB -e /nethome/mct30/err/b2-align.err
#BSUB -o /nethome/mct30/out/b2-align.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

parallel --eta --link \
"/share/apps/bowtie2/2.2.6/bowtie2 -L 10 -f -p 8 --no-unal \
-x /nethome/mct30/bmds/index/{1}-{2}/{1}-{2}_index \
-U /nethome/mct30/bmds/reads/{3}_not_m_s_reads.fa \
-S /nethome/mct30/bmds/SAM_out/{3}_Gut_{2}-only_not_m_s.map" \
::: G006 G006 G002 BTIRed G006 G006 \
::: Myzus Buchnera Buchnera Buchnera Myzus Myzus \
::: G006 G006 G002 BTIRed G002 BTIRed
