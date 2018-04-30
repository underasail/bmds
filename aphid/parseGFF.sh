#! /bin/bash

while read -r a b c d; do
    if [[ $c == 'three_prime_utr' ]]; then
	echo -e "$a\t$b\t$c\t$d"
    fi 
done < G006_Myzus_genome_ref.gff

# bedtools getfasta \
# -fi /nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_scaffold_0.fasta \
# -bed /nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_three_prime_utr.gff \
# -fo /nethome/mct30/bmds/ref_genomes/G006_Myzus_genome_ref_three_prime_utr.fasta