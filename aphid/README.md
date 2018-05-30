# Aphid Gut/Bacteriocyte sRNA Analysis Project

Download genomes for Myzus persicae, Buchnera Aphidicola, and Brassica oleracea var. capitata Wisconsin Golden Acre from AphidBase and NCBI
Use fetchGenomes to collect other bacteria and virus genomes

    Manually select those that don't meet script criteria
    Pulls genomes from literature review into downloaded FASTA files
bowtie2-indexing

    Indexes each of the individual genomes and then the big three together
G006-alignments

    Aligns all three together and each individual alignment with full reads files

elimMatched

    Eliminates the reads that matched perfectly or with one mismatch to Myzus, Buchnera, or plant and generates new FASTA files with only the unmatched reads
    Used later for other bacteria and virus alignments
elimUnmatched

    Eliminates the reads that didn't match perfectly or with one mismatch to Myzus, Buchnera, or plant and generates new FASTA files with only the matched reads
    Used later for miRNA analysis
perSAM-BSUB-pegasus.sh >

    Calculates percentage of reads used in alignment that mapped to the specificed group of genomes
