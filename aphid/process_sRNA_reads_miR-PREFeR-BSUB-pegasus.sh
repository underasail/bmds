#! /bin/bash

#BSUB -J processreads_G002
#BSUB -e /nethome/mct30/err/processreads_G002.err
#BSUB -o /nethome/mct30/out/processreads_G002.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -R "span[ptile=16]"
#BSUB -R "rusage[mem=3000]"
#BSUB -W 24:00
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module switch python/2.7.3

/nethome/mct30/local/miR-PREFeR/miR-PREFeR/scripts/process-reads-fasta.py \
/nethome/mct30/bmds/reads/samplename.txt \
/nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27_SRR799356-58_vdb_cutad_q28_17-25.fasta

# /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_q28.fasta
# /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27.fasta
# /nethome/mct30/bmds/reads/samplename.txt \
# /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants.fasta

/nethome/mct30/local/miR-PREFeR/miR-PREFeR/scripts/bowtie-align-reads.py \
-f -v 0 -p 8 \
-i /nethome/mct30/bmds/index/bt1-plant/bt1-plant-index \
/nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27_SRR799356-58_vdb_cutad_q28_17-25.fasta.processed
# /nethome/mct30/acypi/sra/plants/SRR6517737-46_vdb_ca27.fasta.processed
# /nethome/mct30/bmds/reads/G006_Gut_F_trimmed_17-35_plants-only2.fasta.processed
# -r /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
## -r and -i are mutually exclusive