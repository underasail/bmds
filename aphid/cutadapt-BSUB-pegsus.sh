#! /bin/bash

#BSUB -J cutadapt
#BSUB -e /nethome/mct30/err/cutadapt.err
#BSUB -o /nethome/mct30/out/cutadapt.out
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

module load python/3.6.5

cd /nethome/mct30/acypi/sra/plants



# for adapter in \
# TGAAGCTGCCAGCATGATCTATCGTATGCCGTCTTCTGCTTGAAAAAAA TCGGACCAGGCTTCATTCCCCTCGTATGCCGTCTTCTGCTTGAAAAAAA TCGCTTGGTGCAGGTCGGGACTCGTATGCCGTCTTCTGCTTGAAAAAAA GGCGGATGTAGCCAAGTGGATCGTATGCCGTCTTCTGCTTGAAAAAAAA ACAGGGAACAAGCAGAGCATGTCGTATGCCGTCTTCTGCTTGAAAAAAA ATCCGGGCTAGAAGCGACGCATCGTATGCCGTCTTCTGCTTGAAAAAAA TTGACAGAAGATAGAGAGCACTCGTATGCCGTCTTCTGCTTGAAAAAAA GCGTCTGTAGTCCAACGGTCGTATGCCGTCTTCTGCTTGAAAAAAAAAA TTCTGACTTAGAGGCGTTCAGTCGTATGCCGTCTTCTGCTTGAAAAAAA GCGTCTGTAGTCCAACGGTTCGTATGCCGTCTTCTGCTTGAAAAAAAAA TGAATCTCAGTGGATCGTGGCTCGTATGCCGTCTTCTGCTTGAAAAAAA CGGATTCTGACTTAGAGGCGTTCGTATGCCGTCTTCTGCTTGAAAAAAA TCCGGGCTAGAAGCGACGCATGTCGTATGCCGTCTTCTGCTTGAAAAAA TCAGAATCCGGGCTAGAAGCGTCGTATGCCGTCTTCTGCTTGAAAAAAA TCGCTTGGTGCAGGTCGGGAATCGTATGCCGTCTTCTGCTTGAAAAAAA CTTTGTCTATCGTTTGGAAAAGTCGTATGCCGTCTTCTGCTTGAAAAAA CGGATTCTGACTTAGAGGCGTTTCGTATGCCGTCTTCTGCTTGAAAAAA GGTGAAGTGTTCGGATCGCGGCGTCGTATGCCGTCTTCTGCTTGAAAAA AGAATCTTGATGATGCTGCATTCGTATGCCGTCTTCTGCTTGAAAAAAA TCAGAATCCGGGCTAGAAGCGATCGTATGCCGTCTTCTGCTTGAAAAAA CGGGGTATTGTAAGTGGCAGAGTCGTATGCCGTCTTCTGCTTGAAAAAA TCCGGGCTAGAAGCGACGCATTCGTATGCCGTCTTCTGCTTGAAAAAAA AGAATCCGGGCTAGAAGCGACTCGTATGCCGTCTTCTGCTTGAAAAAAA AAGGCACGTGTCGTTGGCTAATCGTATGCCGTCTTCTGCTTGAAAAAAA TGACAGAAGAGAGTGAGCACTCGTATGCCGTCTTCTGCTTGAAAAAAAA CTGAATCTCAGTGGATCGTGGTCGTATGCCGTCTTCTGCTTGAAAAAAA AATCTCAGTGGATCGTGGCAGCTCGTATGCCGTCTTCTGCTTGAAAAAA TCGCTTGGTGCAGGTCGGGAACTCGTATGCCGTCTTCTGCTTGAAAAAA GGGGATGTAGCTCAGATGGTTCGTATGCCGTCTTCTGCTTGAAAAAAAA GTCAGAATCCGGGCTAGAAGCGACGCATCGTATGCCGTCTTCTGCTTGA CGGGGTATTGTAAGTGGCAGATCGTATGCCGTCTTCTGCTTGAAAAAAA TCTCAGTGGATCGTGGCAGCATCGTATGCCGTCTTCTGCTTGAAAAAAA AGCTCCTACTGAGGGTCGGCATCGTATGCCGTCTTCTGCTTGAAAAAAA TTGACAGAAGAGAGCGAGCACTCGTATGCCGTCTTCTGCTTGAAAAAAA GTCAGAATCCGGGCTAGAAGCGACGCTCGTATGCCGTCTTCTGCTTGAA CCGGATTCTGACTTAGAGGCGTCGTATGCCGTCTTCTGCTTGAAAAAAA AAATCAAGGCGGTCCGGACGGTCGTATGCCGTCTTCTGCTTGAAAAAAA\
# ; do
#     cutadapt -j 8 -a $adapter SRR799356-58_vdb.fastq > SRR799356-58_vdb_ca_$adapter.fastq

# CGTATGCCGTCTTCTGCTTG

for file in /nethome/mct30/acypi/sra/plants/read_files/SRR65177*; do
    cutadapt -j 8 -o $file.fasta $file;
done

# cutadapt -j 8 -a TCGTATGCCGTCTTCTGCTTG -q 28 --minimum-length 17 --maximum-length 25 \
# SRR799356-58_vdb.fastq > SRR799356-58_vdb_cutad_q28_17-25.fastq

# module load fastqc java/1.8.0_60

# export _JAVA_OPTIONS=-Xmx1500m

# cd /nethome/mct30/acypi/sra/plants/fastqc

# /nethome/mct30/local/fastqc/FastQC/fastqc \
# -o ./ -j /share/opt/java/jdk1.8.0_60/bin/java --noextract -t 8 \
# ../