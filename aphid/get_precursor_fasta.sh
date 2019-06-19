#! /bin/bash

tsv_file=/nethome/mct30/bmds/exact_mirs_precursor_info.txt
bed_file=/nethome/mct30/bmds/exact_mirs_precursors.bed
genome_file=/nethome/mct30/bmds/ref_genomes/plants/GCF_000695525.1_BOL_genomic.fasta
fasta_file=/nethome/mct30/bmds/exact_mirs_precursors.fasta

while read -r a b c d e f g h i j k l m; do
    echo ">$a"
    echo $k
done < $tsv_file \
> $fasta_file

#bedtools getfasta -fi $genome_file -bed $bed_file -fo $fasta_file