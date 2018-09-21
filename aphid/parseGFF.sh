#! /bin/bash

#BSUB -J parseGFF
#BSUB -e /nethome/mct30/err/parseGFF.err
#BSUB -o /nethome/mct30/out/parseGFF.out
#BSUB -P acypi
#BSUB -n 1
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


# while read -r a b c d; do
#     if [[ $c == "CDS" ]]; then
# 	echo -e "$a\t$b\t$c\t$d"
#     elif [[ $c == "exon" ]]; then
# 	echo -e "$a\t$b\t$c\t$d"
#     else
# 	true
#     fi 
# done < /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.gff \
# > /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_exclusion.gff

# bedtools getfasta \
# -fi \
# /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
# -bed \
# /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_exclusion.gff \
# -fo \
# /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_exclusion.fasta

# while read -r a b c d e f; do
#     if [[ $c == "CDS" ]]; then
#       true
#     elif [[ $c == "exon" ]]; then
#       true
#     else
#       echo -e "$a:$d-$e\t$c\t$b\t$c\t$d$e\t$f"
#     fi
# done < /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.gff \
# > /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion.gff

while read -r a b c d e f; do
    if [[ $c == "CDS" ]]; then
      true
    elif [[ $c == "exon" ]]; then
      true
    else
      echo -e "$a\t$b\t$c\t$d\t$e\t$f"
    fi
done < /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.gff \
> /nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion_normal.gff

bedtools getfasta \
-fi \
/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta \
-bed \
/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion_normal.gff \
-fo \
/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic_inclusion.fasta