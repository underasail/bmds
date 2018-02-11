# Aphid Gut/Bacteriocyte sRNA Analysis Project

bowtie2-Myzus-Buchnera-split-BSUB-pegasus.sh
    Aligns bacteriocyte and gut reads to Myzus persicae and Buchnera aphidicola individually

bowtie2-Myzus-Buchnera-together-BSUB-pegasus.sh >
    Aligns bacteriocyte and gut reads to Myzus persicae and Buchnera aphidicola together
elimMatched-BSUB-pegasus.sh >
    Eliminates the reads that matched perfectly to Myzus or Buchnera and generates new FASTA files with only the unmatched reads
fetchGenomes-BSUB-pegasus.sh >
    Pulls genomes from literature review into downloaded FASTA files
bowtie2-other_bacteria-viruses-plant-BSUB-pegasus.sh >
    Aligns unmatched reads against literature review organisms
perSAM-BSUB-pegasus.sh >
    Calculates percentage of reads used in alignment that mapped to the specificed group of genomes
