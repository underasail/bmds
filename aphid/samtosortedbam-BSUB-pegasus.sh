#! /bin/bash

#BSUB -J samtosortedbam
#BSUB -e /nethome/mct30/err/samtosortedbam.err
#BSUB -o /nethome/mct30/out/samtosortedbam.out
#BSUB -n 1
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -R "rusage[mem=21000]"
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

cd /nethome/mct30/acypi/sra/plants/ShortStack_0.5rpm_20-24_u_300_showsec_SRA-ca27

# samtools view -bS SRR6517737-46_vdb_ca27_readsorted.sam | \
# samtools sort -@ 8 -m 20000M - -o SRR6517737-46_vdb_ca27_readsorted.sorted.bam

# samtools index SRR6517737-46_vdb_ca27_readsorted.sorted.bai
samtools index SRR6517737-46_vdb_ca27_readsorted.sorted.bam \
SRR6517737-46_vdb_ca27_readsorted.sorted.bai