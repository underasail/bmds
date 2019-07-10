#! /bin/bash

#BSUB -J cutadapt
#BSUB -e /nethome/mct30/err/cutadapt.err
#BSUB -o /nethome/mct30/out/cutadapt.out
#BSUB -n 8
#BSUB -P acypi
#BSUB -q bigmem
#BSUB -W 24:00
#BSUB -w 'done(20722013)'
#BSUB -B
#BSUB -N
#BSUB -u mct30@miami.edu
#
# Job title, error output, standard output, number of cores,
# queue, run time limit, send email when jobs begins, 
# send email with stats when job finished, email,
# default RAM per core is 1500MB

module load python/3.6.5

cd /nethome/mct30/acypi/sra/plants/read_files

# for file in ./SRR79935*fastq; do
#     mv $file ${file%.fastq}_vdb.fastq
# done

module load fastqc java/1.8.0_60

export _JAVA_OPTIONS=-Xmx1500m

cd /nethome/mct30/acypi/sra/plants/fastqc

# for file in /nethome/mct30/acypi/sra/plants/read_files/SRR79935*.fastq; do
#     /nethome/mct30/local/fastqc/FastQC/fastqc \
#     -o ./ -j /share/opt/java/jdk1.8.0_60/bin/java --noextract -t 8 \
#     $file;
# done

# # for file in /nethome/mct30/acypi/sra/plants/read_files/SRR6517737-46_vdb_cutad_q28_17-25.fastq; do
# #     cutadapt -j 8 -o $file.fasta $file;
# # done

# for file in /nethome/mct30/acypi/sra/plants/read_files/SRR79935*.fastq; do
#     cutadapt -j 8 -q 28 --minimum-length 17 --maximum-length 25 \
#     $file > $file\_cutad_q28_17-25.fastq;
# done

# for file in /nethome/mct30/acypi/sra/plants/read_files/SRR79935*.fastq; do
#     trim_galore -q 28 --length 17 --max_length 25 -o /nethome/mct30/acypi/sra/plants/read_files/ $file;
# done


for file in /nethome/mct30/acypi/sra/plants/read_files/SRR79935*trimmed.fq; do
    cutadapt -j 8 -o $file.fasta $file;
done

# # -a TCGTATGCCGTCTTCTGCTTG

# for file in /nethome/mct30/acypi/sra/plants/read_files/SRR79935*cutad_q28_17-25.fastq; do
#     /nethome/mct30/local/fastqc/FastQC/fastqc \
#     -o ./ -j /share/opt/java/jdk1.8.0_60/bin/java --noextract -t 8 \
#     $file;
# done