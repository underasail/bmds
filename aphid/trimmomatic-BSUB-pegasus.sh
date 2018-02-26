#! /bin/bash

#BSUB -J trimmomatic
#BSUB -e /nethome/mct30/err/trimmomatic.err
#BSUB -o /nethome/mct30/out/trimmomatic.out
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


###################################
# G006 Bacteriocyte Read Trimming #
###################################

java -jar /nethome/mct30/trimmomatic/Trimmomatic-0.36/trimmomatic-0.36.jar \
PE -threads 8 -phred33 -trimlog /nethome/mct30/out/G006_trimlog_Bac.log \
/nethome/mct30/bmds/aWilson_G006RNAseq_201344875-01_S_3_1.txt \
/nethome/mct30/bmds/aWilson_G006RNAseq_201344875-01_S_3_2.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344875-01_S_3_1-paired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344875-01_S_3_1-unpaired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344875-01_S_3_2-paired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344875-01_S_3_2-unpaired.txt \
# java -jar <path to trimmomatic.jar> PE (= Paired End) [-threads <threads]
# [-phred33 | -phred64] [-trimlog <logFile>] <input 1> <input 2>
# <paired output 1> <unpaired output 1> <paired output 2>
# <unpaired output 2> <step 1>:option1:option2:etc <step 2> ... <step n>

# ILLUMINACLIP:<fastaWithAdaptersEtc>:<seed mismatches>:
#              <palindrome clip threshold>:<simple clip threshold>
#     fastaWithAdaptersEtc: path to a fasta file containing all the adapters, 
#                           PCR sequences etc.
#     seedMismatches: maximum mismatch count which will still allow a full 
#                     match to be performed
#     palindromeClipThreshold: specifies how accurate the match between the 
#                              two 'adapter ligated' reads must be for PE 
#                              palindrome read alignment.
#     simpleClipThreshold: specifies how accurate the match between any adapter 
#                          etc. sequence must be against a read.
# SLIDINGWINDOW:<windowSize>:<requiredQuality>
#     windowSize: specifies the number of bases to average across
#     requiredQuality: specifies the average quality required.
# LEADING:<quality>
# TRAILING:<quality>
#     quality: Specifies the minimum quality required to keep a base.
# MINLEN:<length>
#     length: Specifies the minimum length of reads to be kept.

##########################
# G006 Gut Read Trimming #
##########################

java -jar /nethome/mct30/trimmomatic/Trimmomatic-0.36/trimmomatic-0.36.jar \
PE -threads 8 -phred33 -trimlog /nethome/mct30/out/G006_trimlog_Gut.log \
/nethome/mct30/bmds/aWilson_G006RNAseq_201344876-01_S_3_1.txt \
/nethome/mct30/bmds/aWilson_G006RNAseq_201344876-01_S_3_2.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344876-01_S_3_1-paired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344876-01_S_3_1-unpaired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344876-01_S_3_2-paired.txt \
/nethome/mct30/bmds/trimmomatic/aWilson_G006RNAseq_201344876-01_S_3_2-unpaired.txt \
